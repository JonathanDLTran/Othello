alpha_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
              "G": 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, "g": 7}
inverted_dict = {alpha_dict[key]: key for key in alpha_dict}


def move(game):
    legal_moves = game.legal_moves
    while True:
        print(game)
        print("Move Choices: " +
              ", ".join([inverted_dict[key].upper() for key in sorted(legal_moves)]))

        col = input("Input the column you want to move to: ")

        move = None
        if col in alpha_dict:
            move = alpha_dict[col]
        elif col.isdigit():
            move = int(col)
        else:
            print(f"Invalid Move: {col} is not a valid column. Try again")
            continue
        if move in legal_moves:
            return move
        print(f"Invalid Move: {move} is not a valid location. Try again")
    return move
