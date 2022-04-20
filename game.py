import random
import matplotlib.pyplot as plt
import numpy as np

"""
How to play:
- 2 Players
- Each player chooses a length 3 sequence of heads or tails
- Computer simulates coin flips until one of the player's length 3 sequence is matched
- Whoever was the player who picked the matching sequence wins that game 
- A race to winning x number of games constitutes a match

e.g 
player1 choice: ['H','H','T']
player2 choice : ['T','T','H']

Coin flip results: 
1) H 
2) T 
3) H 
4) T 
5) T 
6) H

player2 wins this game because the sequence TTH occurred first 
"""


def flip_coin():
    number = random.random()  # random number between 0 and 1
    if number < 0.5:
        return 'T'
    elif number > 0.5:
        return 'H'
    else:  # exactly 0.5, not even sure if this is possible
        print('Miracles do happen')
        return 'S'


def play_game():
    last3 = ['S', 'S', 'S']  # initialise with side coin answer yolo
    while True:
        last3.insert(3, flip_coin())
        last3.pop(0)

        if last3 == player1:
            return 'p1'
        elif last3 == player2:
            return 'p2'


def play_match():
    best_of = race_to * 2 - 1
    player1_scores = [0] * best_of
    player2_scores = [0] * best_of

    count = 0
    while True:
        result = play_game()
        if result == 'p1':
            player1_scores[count] = 1
        else:
            player2_scores[count] = 1

        p1_sum = sum(player1_scores)
        p2_sum = sum(player2_scores)
        print('Player 1: ' + str(p1_sum) + ' Player 2: ' + str(p2_sum))
        if p1_sum == race_to:
            print('Player 1 wins')
            return player1_scores[:count + 1], player2_scores[:count + 1]
        if p2_sum == race_to:
            print('Player 2 wins')
            return player1_scores[:count + 1], player2_scores[:count + 1]

        count += 1


def display_results():
    p1_running_total = np.cumsum(scores1)
    p2_running_total = np.cumsum(scores2)
    x = np.linspace(1, len(p1_running_total), len(p1_running_total))
    plt.plot(x, p1_running_total, label='Player 1')
    plt.plot(x, p2_running_total, label='Player 2')
    plt.xlabel('Game Number')
    plt.ylabel('Score')
    plt.legend()
    if p1_running_total[-1] > p2_running_total[-1]:
        title = 'Player 1 won'
    else:
        title = 'Player 2 won'
    plt.title(title)
    return


if __name__ == "__main__":
    # things you can change
    seed = 2
    race_to = 1000
    player1 = ['H', 'H', 'T']
    player2 = ['T', 'T', 'H']

    # things you shouldn't change
    random.seed(seed)
    scores1, scores2 = play_match()
    display_results()
