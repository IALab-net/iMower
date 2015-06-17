import os
import sys
import numpy as np
import util


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def max_manhattan_distance_heuristic_H(state, problem):
    left_H = util.state_elem_pos(state, 'H', problem.grid_size)
    dist_to_H = [util.manhattan_distance(state[0], xy) for xy in left_H]
    return max(dist_to_H) if len(dist_to_H) else 0


def min_manhattan_distance_heuristic_H(state, problem):
    left_H = util.state_elem_pos(state, 'H', problem.grid_size)
    dist_to_H = [util.manhattan_distance(state[0], xy) for xy in left_H]
    return min(dist_to_H) if len(dist_to_H) else 0


def child_node(problem, parent, action, heuristic):
    new_state = problem.result(parent['state'], action)
    path = parent['path'][:] + [action]
    path_cost = parent['path_cost'] + problem.step_cost(parent['state'], action)
    child = {'state': new_state,
             'path': path,
             'path_cost': path_cost
             }
    return child


def solution(node):
    return node['path']


def graph_search(frontier, problem, heuristic=None, check_frontier=False):
    node = {'state': problem.get_initial_state(), 'path': [], 'path_cost': 0}

    if problem.goal_test(node['state']):
        return solution(node)

    frontier.push(node, node['path_cost'])
    explored = set()

    while not frontier.isEmpty():
        node = frontier.pop()

        if problem.goal_test(node['state']):
            return solution(node)

        explored.add(node['state'])

        for action in problem.actions(node['state']):
            child = child_node(problem, node, action, heuristic)

            if not ((child['state'] in explored) or (frontier.isin(child['state'], fun=lambda x: x['state']) if check_frontier else True)):
                frontier.push(child, child['path_cost'] + (heuristic(child['state'], problem) if heuristic else 0))

        problem._expanded += 1

    raise Exception("Frontier is empty")


def depth_first_search(problem, heuristic=None, check_frontier=False):
    frontier = util.Stack()
    return graph_search(frontier, problem, None, check_frontier)


def breadth_first_search(problem, heuristic=None, check_frontier=False):
    frontier = util.Queue()
    return graph_search(frontier, problem, None, check_frontier)


def uniform_cost_search(problem, heuristic=None, check_frontier=False):
    frontier = util.PriorityQueue()
    return graph_search(frontier, problem, None, check_frontier)


def a_star_search(problem, heuristic, check_frontier=False):
    frontier = util.PriorityQueue()
    return graph_search(frontier, problem, heuristic, check_frontier)
