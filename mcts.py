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

    def add_child(self):
        pass

    def ucb(self):
        return


class MCTS:
    def __init__(self, state, num_trials):
        self.tree = Node(state.getCurrentPlayer(), state)
        self.trials = num_trials

    def search(self):

        for _ in range(self.trials):
            self.selection()
            self.expansion()
            self.simulation()
            self.backpropagation()

    def selection(self):
        pass

    def expansion(self):
        pass

    def simulation(self, node):
        assert type(node) == Node
        assert not node.state.isTerminal()

        actions = node.state.getPossibleActions()
        rewards = 0
        for action in actions:
            childstate = node.state.takeAction(action)
            reward = rollout(childstate)
            rewards += reward

    def backpropagation(self):
        pass


def rollout(state, choice_func=random.choice):
    while not state.isTerminal():
        actions = state.getPossibleActions()
        action = choice_func(actions)
        state = state.takeAction(action)
    return state.getReward()
