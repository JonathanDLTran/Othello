# Inspiration from
# https://github.com/pbsinclair42/MCTS/blob/master/mcts.py
# Some design choices were influecned by pbsinclair42
# But most of the design is mine: I could not figure out how to get theirs to work

import math
import random
from copy import deepcopy

####### CONSTANTS ########

C = math.sqrt(2)

####### CODE #############


class Node:
    def __init__(self, plyr, state):
        self.children = []
        self.player = plyr
        self.state = state
        self.wins = 0
        self.visits = 0
        self.parent = None
        self.action = None

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

    def set_action(self, action):
        self.action = action


class mcts:
    def __init__(self, state, num_trials):
        self.tree = Node(state.getCurrentPlayer(), deepcopy(state))
        self.trials = num_trials

    def search(self):
        for _ in range(self.trials):
            leaf = selection(self.tree)
            if not leaf.state.isTerminal():
                new_node = expansion(leaf)
                reward, action = simulation(new_node)
                new_node.set_action(action)
                backpropagation(new_node, reward, 1)

        child = ucb_select(self.tree.children)
        return child.action


def ucb(node):
    w = node.wins
    n = node.visits
    N = node.parent.visits if node.parent != None else n
    return w/n + C * math.sqrt(math.log(N)/n)


def ucb_select(children):
    assert type(children) == list

    _max = 0
    index = 0
    for i, child in enumerate(children):
        ucb_val = ucb(child)
        if ucb_val > _max:
            _max = ucb_val
            index = i
    return children[index]


def selection(node):
    while not (node.children == []):
        children = node.children
        child = ucb_select(children)
        node = child
    return node


def expansion(node):
    plyr = node.player
    state = node.state
    new_child = Node(not plyr, state)
    new_child.set_parent(node)
    node.add_child(new_child)
    return new_child


def simulation(node, choice_func=random.choice):
    state = deepcopy(node.state)
    first = False
    first_action = None
    while not state.isTerminal():
        actions = state.getPossibleActions()
        action = choice_func(actions)
        if not first:
            first_action = action
            first = True
        state = deepcopy(state.takeAction(action))
    return state.getReward(), first_action


def backpropagation(node, wins, visits=1):
    assert (visits > 0)
    assert (wins <= visits)

    while node.parent != None:
        node.wins += wins
        node.visits += visits
        node = node.parent

    # handle root-most node
    node.wins += wins
    node.visits += visits

    return 0

########## MAIN RUNNER ##########


def main():
    pass


if __name__ == "__main__":
    main()
