#!/usr/bin/python

import curses

import util
from board import Board


def main(stdscr):
    board = Board(4)

    win = util.InitWindow(150)

    keypad_action = {
        curses.KEY_UP: board.MoveUp,
        curses.KEY_LEFT: board.MoveLeft,
        curses.KEY_RIGHT: board.MoveRight,
        curses.KEY_DOWN: board.MoveDown, }

    stdscr.refresh()
    while True:
        pad = win.subpad(board.size()*2+1, board.size()*5+1, 10, 10)
        util.DrawingTiles(pad, board)
        try:
            c = stdscr.getch()
            if c == ord('q'):
                return
            else:
                keypad_action[c]()
                board.NewTile()
        except KeyError:
            pass

    util.TerminatedWindow(win)

if __name__ == "__main__":
    curses.wrapper(main)
