import random
from typing import Tuple, Callable

def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    """
    Calculates the optimal move using the minimax algorithm with alpha-beta pruning.

    :param state: Current game state (instance of GameState).
    :param max_depth: Maximum depth for the search (-1 for unlimited).
    :param eval_func: Evaluation function to assess terminal or leaf states.
                      This function takes a GameState object and the player identifier as arguments,
                      and returns a float representing the utility of the state for the player.
    :return: (int, int) tuple representing the x, y coordinates of the chosen move.
    """
    current_player = state.player
    _, best_move = max(state, float('-inf'), float('inf'), eval_func, max_depth, 0, current_player)
    return best_move

def max(state, alpha, beta, eval_func, max_depth, depth, player) -> Tuple[float, Tuple[int, int]]:
    if state.is_terminal() or (max_depth != -1 and depth >= max_depth):
        return eval_func(state, player), None

    max_value = float('-inf')
    best_move = None

    for action in state.legal_moves():
        successor = state.next_state(action)
        value, _ = min(successor, alpha, beta, eval_func, max_depth, depth + 1, player)
        if value > max_value:
            max_value = value
            best_move = action
        alpha = max(alpha, max_value)
        if alpha >= beta:
            break   # poda beta

    return value, best_move

def min(state, alpha, beta, eval_func, max_depth, depth, player) -> Tuple[float, Tuple[int, int]]:
    if state.is_terminal() or (max_depth != -1 and depth >= max_depth):
        return eval_func(state, player), None

    min_value = float('inf')
    best_move = None

    for action in state.legal_moves():
        successor = state.next_state(action)
        value, _ = max(successor, alpha, beta, eval_func, max_depth, depth + 1, player)
        if value < min_value:
            min_value = value
            best_move = action
        beta = min(beta, min_value)
        if beta <= alpha:
            break   # poda alfa

    return min_value, best_move