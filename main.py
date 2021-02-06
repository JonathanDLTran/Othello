import time
from copy import deepcopy

import othello
import human_player
import mcts_player


def game_loop(game, p1_move, p2_move):

    print("Start of game")
    print(game)
    num_moves = 0
    num_rounds = 0

    while True:
        num_rounds += 1

        print("Player 1 To Move")
        num_moves += 1
        move = p1_move(game)
        game.takeAction(move)

        if game.isTerminal():
            victory = game.getReward()
            if victory > 0:
                print(f"Player 1 Wins : {victory}")
            elif victory == 0:
                print(f"Tie : {victory}")
            else:
                print(f"Player 2 Wins : {victory}")
            print(f"Rounds Played: {num_rounds}")
            print(f"Moves Made: {num_moves}")
            print(game)
            return victory, num_moves
        print(game)

        print("Player 2 To Move")
        num_moves += 1
        move = p2_move(game)
        print(move)
        game.takeAction(move)

        if game.isTerminal():
            victory = game.getReward()
            if victory > 0:
                print(f"Player 2 Wins : {victory}")
            elif victory == 0:
                print(f"Tie : {victory}")
            else:
                print(f"Player 1 Wins : {victory}")
            print(f"Rounds Played: {num_rounds}")
            print(f"Moves Made: {num_moves}")
            print(game)
            return victory, num_moves
        print(game)

        time.sleep(0.05)


def init_game():
    game = othello.State()
    return game


def main(p1_move, p2_move):
    game = init_game()
    game_loop(game, p1_move, p2_move)


def choose_player(player):
    print(f"Choose a player for {'Player 1' if player else 'Player 2'}: ")
    print(f"Type 'H' for human, 'M' for MCTS, 'Q' to quit")
    choice = input("Enter your choice: ")
    choice = choice.strip().lower()
    if choice == 'h':
        return human_player.move
    elif choice == 'm':
        return mcts_player.move
    elif choice == 'q':
        print("Quitting...")
        exit(0)
    else:
        print("Invalid Choice: Try Again")
        print()
        return choose_player(player)


if __name__ == "__main__":
    main(choose_player(True), choose_player(False))
