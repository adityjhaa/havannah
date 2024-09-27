import time
import math
import random
import numpy as np
from helper import *

class Node:
    def __init__(self, state: np.array, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
        self.move = move

    def is_fully_expanded(self):
        return len(self.children) == len(get_valid_actions(self.state))

    def best_child(self, c=1):
        return max(
            self.children, 
            key=lambda x: x.wins / x.visits + c * math.sqrt(2 * math.log(self.visits) / x.visits)
        ) if self.visits > 0 else None

class MCTS:
    def __init__(self, board_size, max_simulations=1000, exploration_constant=1):
        self.board_size = board_size
        self.max_simulations = max_simulations
        self.exploration_constant = exploration_constant

    def run(self, root: Node):
        for _ in range(self.max_simulations):
            node = self.select(root)
            if not self.is_terminal(node.state):
                node = self.expand(node)
            reward = self.rollout(node)
            self.backpropagate(node, reward)

    def select(self, node: Node):
        while not self.is_terminal(node.state):
            if not node.is_fully_expanded():
                return self.expand(node)
            node = node.best_child(self.exploration_constant)
        return node

    def expand(self, node: Node):
        legal_moves = get_valid_actions(node.state)
        for move in legal_moves:
            if move not in [child.move for child in node.children]:
                new_state = self.make_move(node.state, move)
                new_node = Node(new_state, node, move)
                node.children.append(new_node)
                return new_node
        return node

    def rollout(self, node):
        state = node.state.copy()
        current_player = self.get_current_player(state)
        while not self.is_terminal(state):
            valid_moves = get_valid_actions(state)
            if not valid_moves:
                break  # No valid moves available
            move = random.choice(valid_moves)
            state = self.make_move(state, move)
            current_player = 3 - current_player  # Switch players
        return self.get_reward(state)

    def backpropagate(self, node, reward):
        while node is not None:
            node.visits += 1
            node.wins += reward
            node = node.parent

    def make_move(self, state, move):
        new_state = state.copy()
        new_state[move[0], move[1]] = self.get_current_player(state)  # Set the current player's piece
        return new_state

    def is_terminal(self, state):
        return self.check_win_condition(state)

    def get_reward(self, state):
        if self.check_win_condition(state):
            return 1 if self.get_current_player(state) == 1 else 0  # Return 1 for player 1 win, -1 for player 2 win
        return 0.5  # No win

    def check_win_condition(self, board):
        for player in [1, 2]:
            if any([
                self.find_ring(board == player),
                self.find_fork(board == player),
                self.find_bridge(board == player)
            ]):
                return True
        return False

    def find_ring(self, player_board):
        return any(check_ring(player_board, start) for start in get_all_corners(self.board_size))

    def find_fork(self, player_board):
        return any(check_fork(player_board, start) for start in get_all_corners(self.board_size))

    def find_bridge(self, player_board):
        return any(check_bridge(player_board, start) for list_start in get_all_edges(self.board_size) for start in list_start)

    def get_current_player(self, state):
        player_count = [np.sum(state == 1), np.sum(state == 2)]
        return 1 if player_count[0] <= player_count[1] else 2  # Switch based on count

class AIPlayer:

    def __init__(self, player_number: int, timer):
        """
        Intitialize the AIPlayer Agent

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

        board_size = state.shape[0]  # Assuming it's a square board
        self.mcts = MCTS(board_size=board_size, max_simulations=1000)

        # Initialize root node
        root_node = Node(state)
        
        # Run MCTS to find the best move
        self.mcts.run(root_node)
        
        # Select the best move based on the MCTS search
        best_move = root_node.best_child().move
        return best_move
