import random
import time
import copy

import curses

from board import Board


def AutoSolver(board, keypad_actions):
    time.sleep(0.0)
    return MaxSolver(board, keypad_actions)


def BogoSolver(board, keypad_actions):
    return (random.choice(keypad_actions))


def MaxSolver(board, keypad_actions):
    up_board = copy.deepcopy(board)
    up_board.MoveUp()
    down_board = copy.deepcopy(board)
    down_board.MoveDown()
    left_board = copy.deepcopy(board)
    left_board.MoveLeft()
    right_board = copy.deepcopy(board)
    right_board.MoveRight()

    board_act_map = {
        up_board: keypad_actions[0],
        down_board: keypad_actions[1],
        left_board: keypad_actions[2],
        right_board: keypad_actions[3]}

    max_score = max([board.score for board in board_act_map.keys()])
    for board in board_act_map.keys():
        if max_score == board.score:
            return board_act_map[board]


if __name__ == "__main__":
    board = Board(4)
    keypad_actions = {
        curses.KEY_UP: board.MoveUp,
        curses.KEY_DOWN: board.MoveDown,
        curses.KEY_LEFT: board.MoveLeft,
        curses.KEY_RIGHT: board.MoveRight, }
    MaxSolver(board, keypad_actions.keys())
