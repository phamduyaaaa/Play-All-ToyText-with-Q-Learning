# 🎮 Play-All-ToyText with Q-Learning

Welcome to the **Play-All-ToyText with Q-Learning** project! 🚀  
In this project, I've applied the Q-Learning algorithm to solve problems in popular ToyText environments like FrozenLake, CliffWalking, Blackjack, and Taxi.

The goal is to train agents using Q-Learning to optimize policies and maximize rewards in these environments.

---
## 🔍 Introduction

In ToyText environments, agents learn to take actions by maximizing rewards in games such as:

- **FrozenLake** 🌊  
- **CliffWalking** 🧗‍♂️  
- **BlackJack** 🃏  
- **Taxi** 🚕  

The objective of this project is to apply the **Q-Learning** algorithm to optimize agents' policies and achieve the highest possible rewards.

---
### Q-learning Update Rule
The Q-learning update for the Q-table is expressed as:

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
$$

---

### Explanation of Terms


- **$Q(s, a)$:** The current Q-value for performing action $a$ in state $s$.
- **$alpha$ $(Learning Rate)$:** A scalar that controls how much the new information influences the update. Values range from $0$ to $1$.
- **$r$ $(Reward)$:** The immediate reward received after performing action $a$ in state $s$.
- **$gamma$ $(Discount Factor)$:** A scalar between $0$ and $1$ that determines the importance of future rewards. A higher $gamma$ emphasizes long-term rewards.
- **$max_{a'}$ $Q(s', a')$:** The maximum Q-value for the next state $s'$ across all possible actions $a'$.
- **$(s, a)$:** The current state and action pair.
- **$(s', a')$:** The next state and the set of possible actions.

---

### Key Concepts

1. **Temporal Difference (TD) Error:**
   The difference between the expected Q-value and the current Q-value:
   
     $TD\$ $Error$ $=$ $r$ + $\gamma \max_{a'}$ $Q(s', a')$ - $Q(s, a)$

3. **Q-value Update:**
   The Q-value for the current state-action pair $(s, a)$ is updated using the TD error, scaled by the learning rate $(alpha)$. This balances learning from new experiences versus relying on existing knowledge.

4. **Learning Dynamics:**
   - The update incorporates both the immediate reward $r$ and the discounted future rewards $gamma$ $max_{a'}$ $Q(s', a')$.
   - Over time, the Q-table converges to optimal values, assuming sufficient exploration and a properly tuned learning rate.
---

## 🌐 Environments

| Environment | Demo | Plot (Results) |
|-----------------|------|---------------|
| [FrozenLake-v1](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/) | <p align="center"><img src="https://github.com/phamduyaaaa/FrozenLake-with-Q-Learning/blob/main/demo/frozenlake-v1.gif" width="300"></p> | <p align="center"><img src="https://raw.githubusercontent.com/phamduyaaaa/Play-All-ToyText-with-Q-Learning/main/results/frozen.png" width="300"></p> |
| [CliffWalking-v0](https://www.gymlibrary.dev/environments/toy_text/cliff_walking/) | <p align="center"><img src="https://github.com/phamduyaaaa/FrozenLake-with-Q-Learning/blob/main/demo/cliffwalking-v0.gif" width="300"></p> | <p align="center"><img src="https://raw.githubusercontent.com/phamduyaaaa/Play-All-ToyText-with-Q-Learning/main/results/climb.png" width="300"></p> |
| [BlackJack-v1](https://www.gymlibrary.dev/environments/toy_text/blackjack/) | <p align="center"><img src="https://github.com/phamduyaaaa/FrozenLake-with-Q-Learning/blob/main/demo/blackjack-v1.gif" width="300"></p> | <p align="center"><img src="https://raw.githubusercontent.com/phamduyaaaa/Play-All-ToyText-with-Q-Learning/main/results/blackjack.png" width="300"></p> |
| [Taxi-v3](https://www.gymlibrary.dev/environments/toy_text/taxi/) | <p align="center"><img src="https://github.com/phamduyaaaa/FrozenLake-with-Q-Learning/blob/main/demo/taxi-v3.gif" width="300"></p> | <p align="center"><img src="https://raw.githubusercontent.com/phamduyaaaa/Play-All-ToyText-with-Q-Learning/main/results/taxi.png" width="300"></p> |


---


