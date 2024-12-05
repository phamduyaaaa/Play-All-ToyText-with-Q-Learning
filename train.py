import gymnasium as gym
import numpy as np

def q_learning():
    env = gym.make(ENV,is_slippery=False, render_mode="human")
    for epoch in range(EPOCHS):
        state, _ = env.reset()
        total_reward = 0
        steps = 0
        while True:
            action = epsilon_greedy_policy(env, state)
            # action = true_action(env, state)
            next_state, reward, is_done, _, _ = env.step(action)
            Q_table[state, action] = Q_table[state, action] + ALPHA * (reward + GAMMA * np.max(Q_table[next_state, :]) - Q_table[state, action])
            total_reward += reward
            state = next_state
            steps += 1
            if is_done or steps >= MAX_STEPS:
                break
        print_epoch(epoch, steps, total_reward, Q_table)

if __name__ == '__main__':
    q_learning()
