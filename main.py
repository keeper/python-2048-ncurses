#!/usr/bin/python

import curses

import util
from board import Board


def main(*args, **kwds):
  board = Board(5)

  win = util.InitWindow(150)

  while True:
    pad = win.subpad(board.size()*2+1, board.size()*5+1, 10, 10)
    util.DrawingTiles(pad, board)
    c = pad.getch()
    if c == ord('q'):
      break
    else:
      board.NewTile()

  util.TerminatedWindow(win)

if __name__ == "__main__":
  curses.wrapper(main)
