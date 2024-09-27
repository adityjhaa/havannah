import time
import math
import random
import numpy as np
from helper import *

class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0
        self.move = move
        self.terminal_node = False
    
    def is_fully_expanded(self):
        return len(self.children) == len(get_valid_actions(self.state))
    
    def best_child(self, c=1.4):
        """Select the child node with the highest UCB1 score."""
        def ucb_value(child):
            if child.visits == 0:
                return float('inf')  # Prioritize unvisited nodes
            exploitation = child.value / child.visits
            exploration = c * math.sqrt(math.log(self.visits) / child.visits)
            return exploitation + exploration
        
        return max(self.children, key=ucb_value)
    
    def add_child(self, move, state):
        """Add a child node for a given move and state."""
        child_node = Node(state=state, parent=self, move=move)
        self.children.append(child_node)
        return child_node

def mcts(state, timer_per_move, player_number, target_depth=3):
    """
    Monte Carlo Tree Search (MCTS) algorithm with a time limit per move and depth expansion.
    
    Parameters:
        state: np.array -> Current state of the game.
        timer_per_move: float -> Maximum time allowed per move in seconds.
        player_number: int -> The number representing the current player.
        target_depth: int -> The minimum depth of the tree before returning a move.
        
    Returns:
        (int, int): Coordinates of the best move.
    """
    root = Node(state=state)
    start_time = time.time()  # Track the start time of the move
    max_depth_reached = False
    
    while time.time() - start_time < timer_per_move:
        leaf_node, depth = tree_policy(root, player_number, current_depth=0)  # Select a node to explore with depth tracking
        outcome = rollout(leaf_node, player_number)   # Simulate a game from this node
        backpropagate(leaf_node, outcome)             # Backpropagate the result

        # Check if we have reached the target depth
        if depth >= target_depth:
            max_depth_reached = True

        # If we have already expanded to the target depth, we can choose the best move
        if max_depth_reached and time.time() - start_time >= timer_per_move:
            break
    
    # After search, choose the move corresponding to the child with the most visits
    best_move = root.best_child(c=1.41).move  # c=0 means we choose purely based on value/visits
    return best_move

def tree_policy(node, player_number, current_depth):
    """Select a leaf node for exploration using UCB1 and track depth."""
    while not node.terminal_node and current_depth < 3:
        if not node.is_fully_expanded():
            return expand(node, player_number), current_depth + 1  # Expand the node if it's not fully expanded
        else:
            node = node.best_child()  # Select the best child node for exploration
        current_depth += 1
    return node, current_depth

def expand(node, player_number):
    """Expand a node by creating one of its child nodes."""
    valid_moves = get_valid_actions(node.state)
    tried_moves = [child.move for child in node.children]
    
    for move in valid_moves:
        if (move not in tried_moves) and (not is_terminal(node.state, move)):
            new_state = node.state.copy()
            new_state[move] = player_number
            return node.add_child(move, new_state)
        else:
            node.terminal_node = True
    
    return None

def rollout(node, player_number):
    """Simulate a random game from the current node and return the outcome."""
    current_state = node.state.copy()
    current_player = player_number
    
    for _ in range(10):
        move = random.choice(get_valid_actions(current_state))
        if is_terminal(current_state, move):
            node.terminal_node = True
            break
        current_state[move] = current_player
        current_player = 3 - current_player
    
    if check_win(current_state, move, player_number)[0]:
        return 1
    elif check_win(current_state, move, 3 - player_number)[0]:
        return 0
    else:
        return 0.5

def backpropagate(node, outcome):
    """Propagate the result of the simulation back up the tree."""
    while node is not None:
        node.visits += 1
        node.value += outcome
        node = node.parent
        outcome = 1 - outcome

def is_terminal(state, move):
    """
    Check if the current state is terminal, either a win or a draw.
    
    Parameters:
    `state`: The current game state (numpy array)
    
    Returns:
    `bool`: True if the game has ended, otherwise False.
    """
    for player in [1, 2]:
        if (check_win(state, move, player)[0]):
            return True
    return False

class AIPlayer:
    def __init__(self, player_number: int, timer):
        """
        Initialize the AIPlayer Agent

        # Parameters
        `player_number (int)`: Current player number, num==1 starts the game
        
        `timer: Timer`
            - a Timer object that can be used to fetch the remaining time for any player
            - Run `fetch_remaining_time(timer, player_number)` to fetch remaining time of a player
        """
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}: ai'.format(player_number)
        self.timer = timer

    def get_move(self, state: np.array) -> Tuple[int, int]:
        """
        Given the current state of the board, return the next move

        # Parameters
        `state: Tuple[np.array]`
            - a numpy array containing the state of the board using the following encoding:
            - the board maintains its same two dimensions
            - spaces that are unoccupied are marked as 0
            - spaces that are blocked are marked as 3
            - spaces that are occupied by player 1 have a 1 in them
            - spaces that are occupied by player 2 have a 2 in them

        # Returns
        Tuple[int, int]: action (coordinates of a board cell)
        """
        return mcts(state, timer_per_move=5, player_number=self.player_number, target_depth=3)
