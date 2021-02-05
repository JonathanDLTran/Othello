# Inspiration from
# https://github.com/pbsinclair42/MCTS/blob/master/mcts.py
# Some design choices were influecned by pbsinclair42
# But most of the design is mine: I could not figure out how to get theirs to work

import math
import random


class Node:
    def __init__(self, plyr, state):
        self.children = []
        self.player = plyr
        self.state = state
        self.wins = 0
        self.visits = 0
        self.parent = None

    def ucb(self):
        return


class MCTS:
    def __init__(self, trials):
        self.tree = Node(True)
        self.trials = trials

    def selection(self):
        pass

    def expansion(self):
        pass

    def simulation(self, node):
        assert type(node) == Node
        assert not node.state.isTerminal()
        actions = node.getPossibleActions()

    def backpropagation(self):
        pass
