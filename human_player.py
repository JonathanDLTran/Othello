ALPHA_DICT = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, "G": 7, "H": 8,
              'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, "g": 7, "h": 8}
INVERTED_DICT = {ALPHA_DICT[key]: key for key in ALPHA_DICT}
ROWS_LIST = ["1", "2", "3", "4", "5", "6", "7", "8"]


def move(game):
    legal_moves = game.getPossibleActions()
    while True:
        print(game)
        print("Move Choices: " +
              ", ".join([str((INVERTED_DICT[pair[1] + 1].upper(), pair[0] + 1)) for pair in sorted(legal_moves, key=lambda pair: pair[1])]))

        col = input("Input the column you want to move to: ")
        row = input("Input the row you want to move to: ")

        move = None
        if col in ALPHA_DICT:
            col = ALPHA_DICT[col]
        elif col.isdigit():
            col = int(col)
        else:
            print(f"Invalid Move: {col} is not a valid column. Try again")
            continue

        if row in ROWS_LIST:
            row = int(row)
        else:
            print(f"Invalid Move: {row} is not a valid row. Try again")
            continue

        move = (row - 1, col - 1)

        if move in legal_moves:
            return move

        print(f"Invalid Move: {move} is not a valid location. Try again")
