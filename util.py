import curses
from board import Board

def InitWindow(size):
  window = curses.initscr()
  window = curses.newwin(size, size)
  window.keypad(1)
  curses.cbreak()
  curses.noecho()
  return window

def TerminatedWindow(win):
  curses.nocbreak()
  win.keypad(0)
  curses.echo()
  curses.endwin()

def DrawingTiles(pad, board):
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
