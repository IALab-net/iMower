import os
import sys
import util


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def child_node(problem, parent, action, heuristic):
    new_state = problem.result(parent['state'], action)
    path = parent['path'][:] + [action]
    path_cost = parent['path_cost'] + problem.step_cost(parent['state'], action) + (heuristic(new_state, problem) if heuristic else 0)
    child = {'state': new_state,
             'path': path,
             'path_cost': path_cost
             }
    return child


def solution(node):
    return node['path']


def graph_search(frontier, problem, heuristic=None):
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

            if (child['state'] not in explored) and not frontier.isin(child['state'], fun=lambda x: x['state']):
                frontier.push(child, child['path_cost'])

        problem._expanded += 1

    raise Exception("Frontier is empty")


def depth_first_search(problem, heuristic=None):
    frontier = util.Stack()
    return graph_search(frontier, problem, None)


def breadth_first_search(problem, heuristic=None):
    frontier = util.Queue()
    return graph_search(frontier, problem, None)


def uniform_cost_search(problem, heuristic=None):
    frontier = util.PriorityQueue()
    return graph_search(frontier, problem, None)


def a_star_search(problem, heuristic):
    frontier = util.PriorityQueue()
    return graph_search(frontier, problem, heuristic)
