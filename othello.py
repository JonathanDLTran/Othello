"""
othello.py is an implementation of the othello game
"""

######### IMPORTS ###########
from copy import deepcopy

######### CONSTANTS ###########

EMPTY_DISP = "."
BLACK_DISP = "b"
WHITE_DISP = "w"

ALPHA_DISP = "A B C D E F G H"

BLACK = False
WHITE = True
EMPTY = None

WHITE_WIN = 1
TIE = 0
BLACK_WIN = -1

NROWS = 8
NCOLS = 8
"""
INVARIANT: ROW MAJOR : ROW * COL, row first, col second, (y, x)
INVARIANT: WHITE is true, BLACK is false, NOne is unfilled
"""
INIT_BOARD = [[EMPTY for _ in range(NCOLS)] for _ in range(NROWS)]
INIT_BOARD[3][3] = BLACK
INIT_BOARD[3][4] = WHITE
INIT_BOARD[4][3] = WHITE
INIT_BOARD[4][4] = BLACK

######### GAME CLASS CODE ###########


class State:
    """
    STATE IS AN IMPLEMENTATION OF HTE OTHELLO GAME STATE

    INVARIANT: TRUE IS PLAYER 1, FALSE IS PLAYER 2

    ----------------------------------------------------------------------------
    IMPLEMENTS:
    ----------------------------------------------------------------------------
    In order to run MCTS, you must implement a State class which can fully
    describe the state of the world. It must also implement four methods:

    getPossibleActions(): Returns an iterable of all actions which can be
        taken from this state
    takeAction(action): Returns the state which results from taking action
        action
    isTerminal(): Returns whether this state is a terminal state
    getReward(): Returns the reward for this state. Only needed for terminal
        states.
    """

    def __init__(self):
        """
        INVARIANT: TRUE IS PLAYER 1, FALSE IS PLAYER 2
        IMVARIANT WHITE TO MOVE FIRST, E.g TRUE first
        """
        self.board = INIT_BOARD
        self.player = WHITE

    def switch_player(self):
        self.player = not self.player

    def getCurrentPlayer(self):
        return 1 if self.player else -1

    def getPossibleActions(self):
        legal_moves = []
        board = self.board
        plyr = self.player
        other_plyr = not plyr
        for i in range(NROWS):
            for j in range(NCOLS):
                center = board[i][j]
                if center != EMPTY:
                    # NOT EMPTY, cannot place here
                    continue

                found = False
                x = i - 1
                y = j - 1
                if (x >= 0) and (y >= 0) and board[x][y] == other_plyr:
                    x -= 1
                    y -= 1
                    while (x >= 0) and (y >= 0):
                        if board[x][y] == plyr:
                            legal_moves.append((i, j))
                            found = True
                            break
                        elif board[x][y] == EMPTY:
                            break
                        x -= 1
                        y -= 1
                if found:
                    continue

                x = i - 1
                y = j + 1
                if (x >= 0) and (y < NCOLS) and board[x][y] == other_plyr:
                    x -= 1
                    y += 1
                    while (x >= 0) and (y < NCOLS):
                        if board[x][y] == plyr:
                            legal_moves.append((i, j))
                            found = True
                            break
                        elif board[x][y] == EMPTY:
                            break
                        x -= 1
                        y += 1
                if found:
                    continue

                x = i + 1
                y = j - 1
                if (x < NROWS) and (y >= 0) and board[x][y] == other_plyr:
                    x += 1
                    y -= 1
                    while (x < NROWS) and (y >= 0):
                        if board[x][y] == plyr:
                            legal_moves.append((i, j))
                            found = True
                            break
                        elif board[x][y] == EMPTY:
                            break
                        x += 1
                        y -= 1
                if found:
                    continue

                x = i + 1
                y = j + 1
                if (x < NROWS) and (y < NCOLS) and board[x][y] == other_plyr:
                    x += 1
                    y += 1
                    while (x < NROWS) and (y < NCOLS):
                        if board[x][y] == plyr:
                            legal_moves.append((i, j))
                            found = True
                            break
                        elif board[x][y] == EMPTY:
                            break
                        x += 1
                        y += 1
                if found:
                    continue

                x = i
                y = j + 1
                if (y < NCOLS) and board[x][y] == other_plyr:
                    y += 1
                    while (y < NCOLS):
                        if board[x][y] == plyr:
                            legal_moves.append((i, j))
                            found = True
                            break
                        elif board[x][y] == EMPTY:
                            break
                        y += 1
                if found:
                    continue

                x = i
                y = j - 1
                if (y >= 0) and board[x][y] == other_plyr:
                    y -= 1
                    while (y >= 0):
                        if board[x][y] == plyr:
                            legal_moves.append((i, j))
                            found = True
                            break
                        elif board[x][y] == EMPTY:
                            break
                        y -= 1
                if found:
                    continue

                x = i + 1
                y = j
                if (x < NROWS) and board[x][y] == other_plyr:
                    x += 1
                    while (x < NROWS):
                        if board[x][y] == plyr:
                            legal_moves.append((i, j))
                            found = True
                            break
                        elif board[x][y] == EMPTY:
                            break
                        x += 1
                if found:
                    continue

                x = i - 1
                y = j
                if (x >= 0) and board[x][y] == other_plyr:
                    x -= 1
                    while (x >= 0):
                        if board[x][y] == plyr:
                            legal_moves.append((i, j))
                            found = True
                            break
                        elif board[x][y] == EMPTY:
                            break
                        x -= 1
                if found:
                    continue

        return deepcopy(legal_moves)

    def isTerminal(self):
        return self.getPossibleActions() == []

    def count_pieces(self):
        board = self.board
        white_count = 0
        black_count = 0
        for i in range(NROWS):
            for j in range(NCOLS):
                tile = board[i][j]
                if tile == WHITE:
                    white_count += 1
                elif tile == BLACK:
                    black_count += 1
        return (white_count, black_count)

    def getReward(self):
        assert self.isTerminal()
        (white_count, black_count) = self.count_pieces()
        if white_count > black_count:
            if self.player:
                return 1
            else:
                return 0
            # return WHITE_WIN
        elif white_count == black_count:
            return 0
            # return TIE
        else:
            if self.player:
                return 1
            else:
                return 0
            # return BLACK_WIN

    def takeAction(self, action):
        assert type(action) == tuple
        assert len(action) == 2
        assert action in self.getPossibleActions()

        (i, j) = action
        board = self.board
        plyr = self.player
        other_plyr = not plyr
        board[i][j] = plyr

        left = False
        right = False
        up = False
        down = False
        lu = False
        ld = False
        ru = False
        rd = False

        x = i - 1
        y = j - 1
        if (x >= 0) and (y >= 0) and board[x][y] == other_plyr:
            x -= 1
            y -= 1
            while (x >= 0) and (y >= 0):
                if board[x][y] == plyr:
                    ld = True
                    break
                elif board[x][y] == EMPTY:
                    break
                x -= 1
                y -= 1
        x = i - 1
        y = j + 1
        if (x >= 0) and (y < NCOLS) and board[x][y] == other_plyr:
            x -= 1
            y += 1
            while (x >= 0) and (y < NCOLS):
                if board[x][y] == plyr:
                    lu = True
                    break
                elif board[x][y] == EMPTY:
                    break
                x -= 1
                y += 1

        x = i + 1
        y = j - 1
        if (x < NROWS) and (y >= 0) and board[x][y] == other_plyr:
            x += 1
            y -= 1
            while (x < NROWS) and (y >= 0):
                if board[x][y] == plyr:
                    rd = True
                    break
                elif board[x][y] == EMPTY:
                    break
                x += 1
                y -= 1

        x = i + 1
        y = j + 1
        if (x < NROWS) and (y < NCOLS) and board[x][y] == other_plyr:
            x += 1
            y += 1
            while (x < NROWS) and (y < NCOLS):
                if board[x][y] == plyr:
                    ru = True
                    break
                elif board[x][y] == EMPTY:
                    break
                x += 1
                y += 1

        x = i
        y = j + 1
        if (y < NCOLS) and board[x][y] == other_plyr:
            y += 1
            while (y < NCOLS):
                if board[x][y] == plyr:
                    up = True
                    break
                elif board[x][y] == EMPTY:
                    break
                y += 1

        x = i
        y = j - 1
        if (y >= 0) and board[x][y] == other_plyr:
            y -= 1
            while (y >= 0):
                if board[x][y] == plyr:
                    down = True
                    break
                elif board[x][y] == EMPTY:
                    break
                y -= 1

        x = i + 1
        y = j
        if (x < NROWS) and board[x][y] == other_plyr:
            x += 1
            while (x < NROWS):
                if board[x][y] == plyr:
                    right = True
                    break
                elif board[x][y] == EMPTY:
                    break
                x += 1

        x = i - 1
        y = j
        if (x >= 0) and board[x][y] == other_plyr:
            x -= 1
            while (x >= 0):
                if board[x][y] == plyr:
                    left = True
                    break
                elif board[x][y] == EMPTY:
                    break
                x -= 1

        if left:
            x = i - 1
            y = j
            while (x >= 0):
                if board[x][y] == plyr:
                    break
                elif board[x][y] == other_plyr:
                    board[x][y] = plyr
                elif board[x][y] == EMPTY:
                    break
                x -= 1
        if right:
            x = i + 1
            y = j
            while (x < NROWS):
                if board[x][y] == plyr:
                    break
                elif board[x][y] == other_plyr:
                    board[x][y] = plyr
                elif board[x][y] == EMPTY:
                    break
                x += 1

        if up:
            x = i
            y = j + 1
            while (y < NROWS):
                if board[x][y] == plyr:
                    break
                elif board[x][y] == other_plyr:
                    board[x][y] = plyr
                elif board[x][y] == EMPTY:
                    break
                y += 1

        if down:
            x = i
            y = j - 1
            while (y >= 0):
                if board[x][y] == plyr:
                    break
                elif board[x][y] == other_plyr:
                    board[x][y] = plyr
                elif board[x][y] == EMPTY:
                    break
                y -= 1

        if lu:
            x = i - 1
            y = j + 1
            while (x >= 0) and (y < NROWS):
                if board[x][y] == plyr:
                    break
                elif board[x][y] == other_plyr:
                    board[x][y] = plyr
                elif board[x][y] == EMPTY:
                    break
                x -= 1
                y += 1

        if ld:
            x = i - 1
            y = j - 1
            while (x >= 0) and (y >= 0):
                if board[x][y] == plyr:
                    break
                elif board[x][y] == other_plyr:
                    board[x][y] = plyr
                elif board[x][y] == EMPTY:
                    break
                x -= 1
                y -= 1

        if ru:
            x = i + 1
            y = j + 1
            while (x < NCOLS) and (y < NROWS):
                if board[x][y] == plyr:
                    break
                elif board[x][y] == other_plyr:
                    board[x][y] = plyr
                elif board[x][y] == EMPTY:
                    break
                x += 1
                y += 1

        if rd:
            x = i + 1
            y = j - 1
            while (x < NCOLS) and (y >= 0):
                if board[x][y] == plyr:
                    break
                elif board[x][y] == other_plyr:
                    board[x][y] = plyr
                elif board[x][y] == EMPTY:
                    break
                x += 1
                y -= 1

        self.switch_player()

        return deepcopy(self)

    def __str__(self):
        """
        str() is the string represrntation fot eh board
        """
        board = deepcopy(self.board)
        board = reversed(board)

        col = "\t"
        col_count = 8
        for row in board:
            col += f"{col_count} "

            for c in row:
                if c == None:
                    c = EMPTY_DISP
                elif c == BLACK:
                    c = BLACK_DISP
                elif c == WHITE:
                    c = WHITE_DISP
                else:
                    raise RuntimeError(f"Wrong Color: {c}")
                col += (c + " ")

            col += "\n\t"
            col_count -= 1

        col += ("  " + ALPHA_DISP)

        return col

    def __repr__(self):
        """
        repr is same as str()
        """
        return self.__str__()

######### MAIN RUNNER ###########


def main():
    game = State()
    print(game)
    print(game.getPossibleActions())
    game.takeAction((2, 3))
    print(game)
    print(game.getPossibleActions())
    game.takeAction((2, 2))
    print(game)
    print(game.getPossibleActions())
    game.takeAction((4, 5))
    print(game)
    print(game.getPossibleActions())


if __name__ == "__main__":
    main()
