import random
import time


def AutoSolver(board, keypad_actions):
    time.sleep(0.1)
    return BogoSolver(board, keypad_actions)


def BogoSolver(board, keypad_actions):
    return (random.choice(keypad_actions.keys()))
