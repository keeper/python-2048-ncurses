#!/usr/bin/python

import curses

import util
from board import Board

if __name__ == "__main__":
  board = Board(5)

  win = util.InitWindow(100) 

  # These loops fill the pad with letters; this is
  # explained in the next section

  while True:
    pad = win.subpad(board.size()*2+1, board.size()*2+1, 10, 10)
    util.DrawingTiles(pad, board)
    c = pad.getch()
    if c == ord('q'):
      break
    else:
      board.NewTile()

  # Displays a section of the pad in the middle of the screen
util.TerminatedWindow(win)
