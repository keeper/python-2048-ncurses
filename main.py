#!/usr/bin/python

import curses
from board import Board

if __name__ == "__main__":
  board = Board(5)

  win = curses.initscr()
  win = curses.newwin(100, 100)
  # These loops fill the pad with letters; this is
  # explained in the next section

  while True:
    pad = win.subpad(board.size()*2+1, board.size()*2+1, 10, 10)
    for row in range(0, len(board.tiles)):
      for col in range(0, len(board.tiles[row])):
        try:
          pad.addch(row*2+1,col*2+1, ord('0') + board.tiles[row][col])
          pad.addch(row*2+1,col*2+2, '|')
          pad.addch(row*2+2,col*2+1, '-')
          pad.addch(row*2+2,col*2+2, '-')
        except curses.error:
          pass
    pad.box()
    pad.refresh()
    c = pad.getch()
    if c == ord('q'):
      break
    else:
      board.NewTile()

  # Displays a section of the pad in the middle of the screen
  curses.nocbreak(); win.keypad(0); curses.echo()
  curses.endwin()

