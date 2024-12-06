import gymnasium as gym
import numpy as np
import yaml
from utils import *
import csv

def q_learning():
    env = gym.make("Blackjack-v1",natural=False,sab=False, render_mode=MODE)
    player_sum, dealer_card, usable_ace = env.observation_space

    Q_table = np.zeros((player_sum.n, dealer_card.n, usable_ace.n, env.action_space.n))
    for episode in range(NUM_EPISODES):
        state, _ = env.reset()
        player_sum_current , dealer_card_current, usable_ace_current = state
        total_reward = 0
        steps = 0
        EPSILON = max(EPSILON_END, EPSILON_START * (EPSILON_DECAY ** episode))
        while True:
            action = epsilon_greedy_policy(env, state, EPSILON, Q_table)
            next_state, reward, is_done, _, _ = env.step(action)

            Q_table[player_sum_current, dealer_card_current, usable_ace_current, action] = Q_table[player_sum_current, dealer_card_current, usable_ace_current, action] + ALPHA * (reward + GAMMA * np.max(Q_table[next_state, :]) - Q_table[player_sum_current, dealer_card_current, usable_ace_current, action])
            total_reward += reward
            state = next_state
            steps += 1
            if is_done:
                break
        print_blackjack_epoch(episode, steps, total_reward, Q_table)
        writer.writerow([episode, total_reward])
    np.save("Q_table.npy", Q_table)
if __name__ == '__main__':
    with open("blackjack.yaml", "r") as file:
        config = yaml.safe_load(file)
        NUM_EPISODES = config['num_episodes']
        ALPHA = config['alpha']
        GAMMA = config['gamma']
        EPSILON_START = config["epsilon"]["start"]
        EPSILON_END = config["epsilon"]["end"]
        EPSILON_DECAY = config["epsilon"]["decay"]
        NATURAL = config["env"]["natural"]
        SAB = config["env"]["sab"]
        MODE = config["env"]["render_mode"]
    with open("reward_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Episode", "Total Reward"])
        q_learning()
