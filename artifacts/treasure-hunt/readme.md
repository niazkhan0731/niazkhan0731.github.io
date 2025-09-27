# 🏴‍☠️ Treasure Hunt Reinforcement Learning Agent (CS-499 Artifact)

## Overview
The **Treasure Hunt RL Agent** is a reinforcement learning project built in **Python** using **TensorFlow/Keras**.  
It was originally developed as part of the **CS-370 Emerging Trends in Computer Science** course to explore **deep Q-learning** in a custom grid-world environment.  
For my **CS-499 Computer Science Capstone**, I enhanced this artifact to improve the training loop, model architecture, and overall usability.

---

## 🎮 Features
- **Custom 8x8 Maze Environment**: Agent must navigate to treasure while avoiding traps.  
- **Deep Q-Learning (DQN)**: Neural network learns policies through exploration and replay.  
- **Experience Replay Buffer**: Stores past experiences for stable training.  
- **Epsilon-Greedy Strategy**: Balances exploration vs. exploitation.  
- **Visualization Tools**: Environment rendering with agent, traps, and treasure.  

---

## 🛠️ Original Implementation
The original artifact included:
- A **basic DQN setup** using Keras.  
- A grid-world environment with simple rules (reward for treasure, penalty for traps).  
- Training loop with minimal optimization.  
- Demonstrated understanding of **reinforcement learning fundamentals** but lacked refinement for efficiency and clarity.  

---

## 🚀 Enhancements (CS-499)
As part of my **Capstone portfolio**, I improved the artifact by:

1. **Model Architecture**
   - Replaced simple dense layers with a deeper neural network.  
   - Added **PReLU activation** for better gradient learning.  

2. **Training Loop**
   - Enhanced the replay buffer and minibatch training logic.  
   - Added **epsilon decay** and early stopping heuristics.  
   - Improved logging for episode rewards, steps, and win rates.  

3. **Code Quality**
   - Refactored for readability and modularity.  
   - Added helper functions like `format_time()` for clean output.  
   - Better exception handling and comments.  

4. **Visualization**
   - Improved environment display with traps, treasure, and agent states.  
   - Allowed consistent seeding for reproducible runs.  

---

## 🎓 Reflection
This project demonstrates my ability to:
- Apply **algorithms and data structures** in reinforcement learning.  
- Design and evaluate solutions using **deep Q-learning**.  
- Enhance existing code with **performance, readability, and usability improvements**.  

It is included in my **CS-499 Capstone Portfolio** to showcase my skills in **machine learning, neural networks, and algorithmic problem-solving**.

---
