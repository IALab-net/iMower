import os
import sys
import util


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. This heuristic is trivial.
    """
    return 0

# TODO: Define your heuristic


def child_node(problem, parent, action):
    new_state = problem.result(parent['state'], action)
    path = parent['path'][:] + [action]
    path_cost = parent['path_cost'] + problem.step_cost(parent['state'], action)
    child = {'state': new_state,
             'path': path,
             'path_cost': path_cost
             }
    return child


def graph_search(frontier, problem, heuristic=None):
    node = {'state': problem.get_initial_state(), 'path': [], 'path_cost': 0}

    # TODO: Check if the current state is a goal state. If so, return the path argument of the node
    # HINT: Check the definition of a problem in the python_helper.py

    # TODO: Push the current state to the frontier and initialize an explored set

    while not frontier.isEmpty():
        # TODO: Pop the first element from the frontier

        # TODO: Check if it is a goal state. If so, return the path argument of the node

        # TODO: Add the node to the explored set

        for action in problem.actions(node['state']):
            # TODO: define the child node resulting from the action

            # TODO: Push the child node to the frontier if it isn't in the explored set

            problem._expanded += 1


def depth_first_search(problem, heuristic=None):
    # TODO: Initialize the right type of frontier
    # HINT: check for possibilities in util.py
    frontier = "<FILL IN>"
    graph_search(frontier, problem, None)
    raise NotImplementedError


def breadth_first_search(problem, heuristic=None):
    # TODO: Initialize the right type of frontier
    # HINT: check for possibilities in util.py
    frontier = "<FILL IN>"
    graph_search(frontier, problem, None)
    raise NotImplementedError


def uniform_cost_search(problem, heuristic=None):
    # TODO: Initialize the right type of frontier
    # HINT: check for possibilities in util.py
    frontier = "<FILL IN>"
    graph_search(frontier, problem, None)
    raise NotImplementedError


def a_star_search(problem, heuristic):
    # TODO: Initialize the right type of frontier
    # HINT: check for possibilities in util.py
    frontier = "<FILL IN>"
    graph_search(frontier, problem, heuristic)
    raise NotImplementedError
