import random
from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    def alpha_beta(state, depth, alpha, beta, maximizing_player):

        if all(cell == '.' for row in state.board.board for cell in row):
            return (1, 1)  
        if depth == 0 or state.is_terminal():
            return eval_func(state, state.player)

        best_move = None
        if maximizing_player:
            max_eval = float('-inf')
            for move in state.legal_moves():
                new_state = state.next_state(move)
                eval_value = alpha_beta(new_state, depth - 1, alpha, beta, False)
                if eval_value > max_eval:
                    max_eval = eval_value
                    best_move = move
                alpha = max(alpha, eval_value)
                if beta <= alpha:
                    break
            return best_move if depth == max_depth else max_eval
        else:
            min_eval = float('inf')
            for move in state.legal_moves():
                new_state = state.next_state(move)
                eval_value = alpha_beta(new_state, depth - 1, alpha, beta, True)
                if eval_value < min_eval:
                    min_eval = eval_value
                    best_move = move
                beta = min(beta, eval_value)
                if beta <= alpha:
                    break
            return best_move if depth == max_depth else min_eval

    return alpha_beta(state, max_depth, float('-inf'), float('inf'), state.player == 'B')