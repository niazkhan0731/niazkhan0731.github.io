# GameExperience.py
# Replay buffer and training data utilities for Q-learning (tabular or NN-backed).
# Focus: clear data structure (ring buffer) + reproducible sampling.

from collections import deque, namedtuple
import random
import numpy as np

Transition = namedtuple("Transition", ["envstate", "action", "reward", "envstate_next", "game_over"])

class GameExperience(object):
    """
    Experience memory with ring buffer semantics and seeded RNG for reproducibility.
    This class is model-agnostic: it only needs a Keras-like model that supports .predict(batch, verbose=0).
    """

    def __init__(self, model, max_memory=10000, discount=0.95, seed=42):
        self.model = model
        self.max_memory = max_memory
        self.discount = discount
        self.memory = deque(maxlen=max_memory)   # ring buffer
        # infer number of actions from model output (Dense softmax/linear head)
        self.num_actions = int(self.model.output_shape[-1])
        self.rng = random.Random(seed)

    def remember(self, episode):
        """
        Add a transition.
        episode = [envstate, action, reward, envstate_next, game_over]
        Each envstate should be np.ndarray with shape (1, env_features)
        """
        self.memory.append(Transition(*episode))

    def __len__(self):
        return len(self.memory)

    def predict(self, envstate):
        """
        Predict Q-values for a single state (envstate must be batch-shaped).
        Returns a 1D array of Q-values for each action.
        """
        q = self.model.predict(envstate, verbose=0)
        # Allow both (1, A) and (A,) shapes
        q = q[0] if q.ndim == 2 else q
        return q

    def get_data(self, batch_size=32):
        """
        Uniformly sample a minibatch from memory and build (inputs, targets)
        for supervised TD(0) training with the Bellman update.
        Targets are the current Q(s,·) with the action index replaced by TD target.

        Returns:
            inputs  : (B, env_features)
            targets : (B, num_actions)
        """
        mem_size = len(self.memory)
        if mem_size == 0:
            raise ValueError("Replay memory is empty.")
        batch_size = min(mem_size, batch_size)

        # infer env feature size from first transition
        first_state = self.memory[0].envstate
        if first_state.ndim != 2 or first_state.shape[0] != 1:
            raise ValueError("Each envstate must be shaped as (1, features).")
        env_features = first_state.shape[1]

        inputs = np.zeros((batch_size, env_features), dtype=np.float32)
        targets = np.zeros((batch_size, self.num_actions), dtype=np.float32)

        # sample distinct indices
        idxs = self.rng.sample(range(mem_size), k=batch_size)

        for i, j in enumerate(idxs):
            s, a, r, s2, done = self.memory[j]
            # current Q(s,·)
            q_s = self.predict(s).astype(np.float32)
            # bootstrap Q(s',·)
            if done:
                td_target = r
            else:
                q_s2 = self.predict(s2)
                td_target = r + self.discount * float(np.max(q_s2))

            # supervised regression target: copy q_s then replace the taken action's value
            q_s[a] = td_target

            inputs[i] = s[0]      # drop batch dim
            targets[i] = q_s

        return inputs, targets