import numpy as np
from colorama import Fore

def epsilon_greedy_policy(env, state):
    if np.random.rand() < EPSILON:
        action = env.action_space.sample()  # Explore
    else:
        action = np.argmax(Q_table[state, :])  # Exploit
    return action
  
def true_action(state):
    return np.argmax(Q_table[state, :])
  
def print_epoch(epoch, steps, total_reward, Q_table):
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + f"{'Epoch':<10} | {'Steps':<10} | {'Total Reward':<10}")
    print(Fore.CYAN + "-" * 50)
    print(Fore.GREEN + f"{epoch:<10} | {steps:<10} | {total_reward:<10.2f}")
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "Q-Table:")
    print(Fore.CYAN + "-" * 50)

    header = f"{'State':<8} | {'LEFT':>10} | {'DOWN':>10} | {'RIGHT':>10} | {'UP':>10}"
    print(Fore.LIGHTMAGENTA_EX + header)
    print(Fore.CYAN + "-" * 50)

    for state, actions in enumerate(Q_table):
        row = f"{state:<8} | " + " | ".join(f"{q_val:>10.4f}" for q_val in actions)
        print(Fore.WHITE + row)

    print(Fore.CYAN + "=" * 50)
    print("\n")
