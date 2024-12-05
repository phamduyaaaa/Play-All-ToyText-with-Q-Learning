import gymnasium as gym
import numpy as np
import yaml
from utils import *

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)
    NUM_EPISODES = config['epochs']
    ALPHA = config['alpha']
    GAMMA = config['gamma']
    MODE = config['mode']
    MAX_STEPS = config['max_steps']
    EPSILON = config['epsilon']
    ENV = config['env']

def q_learning():
    env = gym.make(ENV,is_slippery=False, render_mode=MODE)
    Q_table = np.zeros((env.observation_space.n, env.action_space.n))
    for episode in range(NUM_EPISODES):
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
