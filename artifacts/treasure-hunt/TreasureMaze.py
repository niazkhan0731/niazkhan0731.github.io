# TreasureMaze.py
# A small grid-world with a Gym-like API for a treasure-hunt agent.

from __future__ import annotations
import numpy as np
import random
from typing import Tuple, Set, Dict, Any, List

# Actions
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
ACTIONS = (UP, RIGHT, DOWN, LEFT)

class TreasureMaze:
    """
    Grid convention:
      0 -> free
      1 -> wall/blocked
    Start, goal, and traps are given as (row, col) tuples.
    Observation: one-hot of agent position (rows*cols). If you need (row,col) pair,
    adapt observe() accordingly.
    """

    def __init__(self,
                 grid: List[List[int]],
                 start: Tuple[int, int],
                 goal: Tuple[int, int],
                 traps: List[Tuple[int, int]] | None = None):
        self.grid = np.array(grid, dtype=np.int32)
        self.nrows, self.ncols = self.grid.shape
        self.start = tuple(start)
        self.goal = tuple(goal)
        self.traps: Set[Tuple[int, int]] = set(map(tuple, traps or []))

        self.n_actions = 4
        self.pos = self.start
        self.mode = "start"
        self.rng = random.Random()
        self.visited: Set[Tuple[int, int]] = set()

    # ---------------- Gym-like API ----------------

    def set_seed(self, seed: int | None):
        self.rng.seed(seed)
        np.random.seed(seed if seed is not None else None)

    def reset(self, seed: int | None = None):
        if seed is not None:
            self.set_seed(seed)
        self.pos = self.start
        self.mode = "start"
        self.visited = set()
        return self.observe()

    def step(self, action: int):
        """Take an action; return (next_state, reward, done, info)"""
        self._update_state(action)
        reward = self._get_reward()
        done = self._is_terminal()
        return self.observe(), reward, done, {}

    # ---------------- Helpers ----------------

    def _in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.nrows and 0 <= c < self.ncols

    def valid_actions(self) -> List[int]:
        """Actions that would keep you inside the grid (ignores walls here)."""
        r, c = self.pos
        actions = []
        if self._in_bounds(r - 1, c): actions.append(UP)
        if self._in_bounds(r, c + 1): actions.append(RIGHT)
        if self._in_bounds(r + 1, c): actions.append(DOWN)
        if self._in_bounds(r, c - 1): actions.append(LEFT)
        return actions

    def _update_state(self, action: int):
        """Update internal state given action; set mode to 'valid' or 'invalid'."""
        r, c = self.pos

        nr, nc = r, c
        if action == UP:    nr -= 1
        if action == RIGHT: nc += 1
        if action == DOWN:  nr += 1
        if action == LEFT:  nc -= 1

        # out of bounds
        if not self._in_bounds(nr, nc):
            self.mode = "invalid"
            # do not move
            return

        # wall
        if self.grid[nr, nc] == 1:
            self.mode = "blocked"
            # do not move
            return

        # valid move
        self.pos = (nr, nc)
        self.mode = "valid"
        self.visited.add(self.pos)

    def _get_reward(self) -> float:
        """Simple, explainable shaping:
           -1 per step,
           -5 if bumped into a wall/out-of-bounds (invalid/blocked),
           +10 for treasure,
        """
        if self.mode in ("invalid", "blocked"):
            return -5.0
        if self.pos == self.goal:
            return +10.0
        if self.pos in self.traps:
            return -5.0
        return -1.0  # small living penalty to encourage shortest path

    def _is_terminal(self) -> bool:
        return self.pos == self.goal

    def observe(self) -> np.ndarray:
        """Return a (1, nrows*ncols) one-hot of agent position."""
        idx = self.state_index(self.pos)
        one_hot = np.zeros((1, self.nrows * self.ncols), dtype=np.float32)
        one_hot[0, idx] = 1.0
        return one_hot

    def state_index(self, pos: Tuple[int, int]) -> int:
        r, c = pos
        return r * self.ncols + c

    # Optional text render for debugging
    def render(self) -> None:
        canvas = np.full((self.nrows, self.ncols), " ")
        for r in range(self.nrows):
            for c in range(self.ncols):
                if self.grid[r, c] == 1:
                    canvas[r, c] = "#"
        for (tr, tc) in self.traps:
            canvas[tr, tc] = "X"
        gr, gc = self.goal
        canvas[gr, gc] = "T"
        r, c = self.pos
        canvas[r, c] = "P"
        print("\n".join("".join(row) for row in canvas))
