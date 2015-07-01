# PYTHON STRUCTURES

# ---- List
my_empty_list = [] # Initialize an emply list
my_list = [1,2,3,4]
my_list[0] # Access first element of list

# ---- Set
my_set = set() # Initialize a set
my_set.add('toto') # Add an element to the set
'toto' in my_set # Check if 'toto' is in the set

# ---- Dictionary
my_dico = {'toto': 1, 'titi': 2, 'tata': 3} # Initialize a dictionary
my_dico['toto'] # Access a dictionary element
my_dico['tutu'] = 4 # Add an element to dictionary


# PYTHON FUNCTIONS

# ---- Definition of a function
def my_function(arg1, arg2):
	# Some instructions
	return my_result


# DEFINITION OF A PROBLEM

# ---- Arguments
_grid # The grid world (Array)
grid_size # Height and widht of the grid
elems_state # The grid as a string
_e_ij # The position in the string grid given its coordinates
_initial_state # Tuple (mower_position, elems_state, nb_propellers)
_penalties # Penalties dictionary (elements are "living", "mow_to_earth" and "lose_propeller")
_earth_mode # Boolean to specify if we can mow until the earth or not (defaut False)
_expanded # Number of nodes expanded in the graph search

# ---- Methods
def get_initial_state(self): # Returns the initial state tuple

def goal_test(self, state): # Boolean, True if the state considered is a goal state

def is_game_over(self, state): # Boolean, True if nb_propellers = 0

def actions(self, state): # List of all possible actions given a state

def result(self, state, action): # New state tuple, which is the result of the an action taken at a given state

def step_cost(self, state, action): # The cost of an action taken at a given state

def get_path_cost(self, actions): # The overal cost given all actions taken since the initial state



# DEFINITION OF A STATE

# ---- Arguments
grid # The world grid
_mower_pos # The position of the mower in the grid
_earth_mode # Boolean, True if the mower can mow until the earth
_nb_propellers # Number of propellers of the mower
_bonus_mow # The bonus given when we mow
_score # The score of the mower
_penalties # Dictionary of penalties (living_penalty, mow_to_earth, lose_propeller)

# ---- Methods
def get_grid_size(self): # Height and widht of the grid

def is_game_over(self): # Boolean, True if nb_propellers = 0

def is_win(self): # Boolean, True if there is no mode 'H' in the grid

def execute_action(self, action): # Returns final state given a set of actions