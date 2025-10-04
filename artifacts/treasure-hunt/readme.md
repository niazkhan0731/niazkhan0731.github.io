# 🏴‍☠️ Treasure Hunt Reinforcement Learning Agent

## 📖 Overview
This project implements a reinforcement learning (RL) agent designed to solve a **Treasure Hunt maze** game. The environment is represented as a grid where the agent (a pirate) must navigate around traps and walls to reach the treasure. The agent uses **Deep Q-Learning (DQN)** to learn the optimal strategy through trial and error.

Originally developed in **CS 370: Current/Emerging Trends in Computer Science**, this artifact was later enhanced in **CS 499: Computer Science Capstone** to improve its algorithms and structure.

---

## 🏗️ Original Implementation
- Used a basic Q-Learning setup with:
  - A maze environment (`TreasureMaze.py`)
  - An experience replay buffer (`GameExperience.py`)
  - A Jupyter Notebook (`TreasureHuntGame.ipynb`) to run and test the agent
- Focused on:
  - Representing the maze as a state matrix
  - Allowing the pirate agent to take actions (UP, DOWN, LEFT, RIGHT)
  - Rewarding successful treasure discovery and penalizing traps

---

## ✨ Enhancements Made
As part of **Milestone Three: Algorithms and Data Structures**, the artifact was updated to demonstrate stronger reinforcement learning techniques and cleaner structure:

- **Deep Q-Network (DQN):**  
  Replaced the basic Q-learning logic with a **neural network** built in TensorFlow/Keras for approximating Q-values.
  
- **Custom Q-Network Architecture:**  
  - Two hidden layers with **PReLU activations** for adaptive learning  
  - Optimized with **Adam optimizer**  
  - More efficient state-to-action mapping

- **Replay Buffer:**  
  Improved `GameExperience` class to store and sample experiences for stable training.

- **Training Loop:**  
  Implemented an epsilon-greedy policy with decay, warm-up period, and early stopping for better training efficiency.

- **Reproducibility:**  
  Added fixed random seeds and numpy print settings for consistent experiments.

- **Visualization:**  
  Improved maze visualizations to show agent state, traps, and treasure during runs.

---

## 🔧 Tech Stack
- **Language:** Python 3.11  
- **Libraries:** TensorFlow (with Metal acceleration on macOS), NumPy, Matplotlib  
- **Environment:** Jupyter Notebook  

---

## 🚀 How to Run
1. Clone the repo and navigate to the project folder:
   ```bash
   git clone https://github.com/niazkhan0731/niazkhan0731.github.io
   cd artifacts/treasure-hunt

