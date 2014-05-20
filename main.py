#!/usr/bin/python

import curses
import random

import drawing
import autosolver
from board import Board


def main(stdscr):
    size = 4
    board_length, board_width = size * 5 + 1, size * 2 + 1
    pad_pos_x, pad_pos_y = 5, 7
    board = Board(size)
    auto = False

    win = drawing.InitWindow(150)

    keypad_actions = {
        curses.KEY_UP: board.MoveUp,
        curses.KEY_DOWN: board.MoveDown,
        curses.KEY_LEFT: board.MoveLeft,
        curses.KEY_RIGHT: board.MoveRight, }

    win.addstr(1, 0, "Arrow keys to move tiles");
    win.addstr(2, 0, "a to enable auto solver");

    win.addstr(5, 0, "Score: " + str(board.score))
    pad = win.subpad(
        board_width, board_length,
        pad_pos_y, pad_pos_x)
    stdscr.refresh()
    win.refresh()
    while True:
        drawing.DrawingTiles(pad, board)
        try:
            if not auto:
                c = stdscr.getch()
            else:
                c = autosolver.AutoSolver(board, keypad_actions.keys())
            if c == ord('a'):
                auto = not auto
            if c == ord('q'):
                return
            else:
                moved = keypad_actions[c]()
                if moved:
                    board.NewTile()
                    drawing.DrawingTiles(pad, board)
                    win.addstr(5, 0, "Score: " + str(board.score))
                    win.refresh()
                if len(board.empty_pos()) == 0:
                    if board.GameOver():
                        drawing.GameOverMsg(
                            pad_pos_y + board_width, 0,
                            board, stdscr)
                        if stdscr.getch() == ord('r'):
                            return main(stdscr)
                        return
        except KeyError:
            pass

    drawing.TerminatedWindow(win)

if __name__ == "__main__":
    curses.wrapper(main)
