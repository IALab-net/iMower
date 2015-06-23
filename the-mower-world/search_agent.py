import time
import numpy as np
from game import move, is_in_grid, elem_rules_trans


class MowSearchProblem():
    def __init__(self, starting_gameState):
        self._grid = starting_gameState._grid
        self.grid_size = self._grid.shape
        elems_state = self._grid.tostring()
        self._e_ij = lambda i, j: i * self._grid.shape[1] + j
        self._initial_state = (starting_gameState._mower_pos, elems_state, starting_gameState._nb_propellers)
        self._penalties = starting_gameState._penalties
        self._earth_mode = starting_gameState._earth_mode
        self._expanded = 0

    def get_initial_state(self):
        return self._initial_state

    def goal_test(self, state):
        return 'H' not in state[1]

    def is_game_over(self, state):
        return state[2] == 0

    def actions(self, state):
        if self.is_game_over(state):
            return "STOP"
        la = np.array(['UP', 'DOWN', 'RIGHT', 'LEFT'])
        is_legals_actions = np.array([is_in_grid(move(state[0], a), self._grid.shape) for a in la])
        return la[is_legals_actions].tolist()

    def result(self, state, action):
        pos = state[0]
        elems_state = list(state[1])
        nb_propellers = state[2]

        next_pos = move(pos, action)

        if is_in_grid(next_pos, self._grid.shape):
            pos = next_pos
            ind_next_e = self._e_ij(*next_pos)
            next_e = elems_state[ind_next_e]

            if next_e == 'R':
                nb_propellers = max(nb_propellers - 1, 0)

            elems_state[ind_next_e] = elem_rules_trans(next_e, self._earth_mode)

        return (pos, ''.join(elems_state), nb_propellers)

    def step_cost(self, state, action):
        cost = 0
        pos = state[0]
        elems_state = state[1]
        nb_propellers = state[2]
        next_pos = move(pos, action)
        ind_next_e = self._e_ij(*next_pos)
        next_e = elems_state[ind_next_e]
        if next_e == 'R':
            if nb_propellers > 1:
                cost += self._penalties['lose_propeller']
            else:
                return 999999
        if (next_e == 'L') and self._earth_mode:
            cost += self._penalties['mow_to_earth']

        cost += self._penalties['living']
        return cost

    def get_path_cost(self, actions):
        state = self._initial_state
        cost = 0
        for action in actions:
            cost += self.step_cost(state, action)
            state = self.result(state, action)
        return cost


class SearchAgent:
    def __init__(self, problem, search_fun, heuristic=lambda state, problem=None: 0, check_frontier=False):
        self._problem = problem
        self._search_fun = search_fun
        self._heuristic = heuristic
        self._check_frontier = check_frontier

    def plan(self):
        start_time = time.time()
        self._actions = self._search_fun(self._problem, self._heuristic, self._check_frontier)
        self._actions_iterator = (a for a in self._actions)
        total_cost = self._problem.get_path_cost(self._actions)

        print('Path found with total cost of %d in %.1f seconds' % (total_cost, time.time() - start_time))
        print('Search nodes expanded: %d' % self._problem._expanded)

    def get_action(self):
        try:
            return self._actions_iterator.next()
        except:
            return "STOP"
