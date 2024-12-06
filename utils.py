import numpy as np
from colorama import Fore

def epsilon_greedy_policy(env, state, EPSILON, Q_table):
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
    
def print_blackjack_epoch(epoch, steps, total_reward, Q_table):
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + f"{'Epoch':<10} | {'Steps':<10} | {'Total Reward':<10}")
    print(Fore.CYAN + "-" * 50)
    print(Fore.GREEN + f"{epoch:<10} | {steps:<10} | {total_reward:<10.2f}")
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "Q-Table:")
    print(Fore.CYAN + "-" * 50)

    # Header for the Q-table
    header = f"{'State':<25} | {'Stick':>10} | {'Hit':>10}"
    print(Fore.LIGHTMAGENTA_EX + header)
    print(Fore.CYAN + "-" * 50)

    # Iterate through the Q-table to print values
    for player_sum in range(1, 22):  # Player's sum from 1 to 21
        for dealer_card in range(1, 11):  # Dealer's card from 1 to 10
            for usable_ace in [False, True]:  # Usable Ace: False or True
                state = f"({player_sum}, {dealer_card}, {usable_ace})"
                actions = Q_table[player_sum - 1, dealer_card - 1, int(usable_ace)]
                row = f"{state:<25} | {actions[0]:>10.4f} | {actions[1]:>10.4f}"
                print(Fore.WHITE + row)

    print(Fore.CYAN + "=" * 50)
    print("\n")
