#!/usr/bin/python

import curses

import drawing
from board import Board


def main(stdscr):
    size = 4
    board = Board(size)

    win = drawing.InitWindow(150)

    keypad_action = {
        curses.KEY_UP: board.MoveUp,
        curses.KEY_LEFT: board.MoveLeft,
        curses.KEY_RIGHT: board.MoveRight,
        curses.KEY_DOWN: board.MoveDown, }

    win.addstr(5, 0, "Score: " + str(board.score))
    pad = win.subpad(board.size()*2+1, board.size()*5+1, 7, 5)
    stdscr.refresh()
    win.refresh()
    while True:
        drawing.DrawingTiles(pad, board)
        try:
            c = stdscr.getch()
            if c == ord('q'):
                return
            else:
                moved = keypad_action[c]()
                if moved:
                    board.NewTile()
                elif len(board.empty_pos()) == 0:
                    if board.GameOver():
                        break
                win.addstr(5, 0, "Score: " + str(board.score))
                win.refresh()
        except KeyError:
            pass

    drawing.TerminatedWindow(win)

if __name__ == "__main__":
    curses.wrapper(main)
