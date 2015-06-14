import os
import sys
import util


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def depth_first_search(problem, heuristic=None):
    raise NotImplementedError


def breadth_first_search(problem, heuristic=None):
    raise NotImplementedError


def uniform_cost_search(problem, heuristic=None):
    raise NotImplementedError


def a_star_search(problem, heuristic):
    raise NotImplementedError
