from mcts import mcts

from copy import deepcopy


def move(game):
    searcher = mcts(deepcopy(game), 100)
    return searcher.search()
