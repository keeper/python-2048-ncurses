import curses
from board import Board


def InitWindow(size):
    window = curses.newwin(size, size)
    color_list = [
        curses.COLOR_WHITE, curses.COLOR_YELLOW,
        curses.COLOR_RED, curses.COLOR_GREEN,
        curses.COLOR_CYAN, curses.COLOR_MAGENTA,
        curses.COLOR_RED, ]

    for i in range(len(color_list)):
        curses.init_pair(i+1, color_list[i], curses.COLOR_BLACK)
    window.keypad(1)
    return window


def TerminatedWindow(win):
    win.keypad(0)


def DrawingTiles(pad, board):
    pad.box()
    for row in range(len(board.tiles)):
        for col in range(len(board.tiles[row])):
            try:
                ColoringTiles(row, col, board, pad)
            except curses.error:
                pass
    pad.refresh()


def DrawingNumber(row, col, board, pad, num_color):
    num = board.tiles[row][col]
    num_str = ""
    if num == 0:
        num_str = " " * 4
    else:
        num_str = str(num)
    for i in range(len(num_str), 4):
        num_str = " " + num_str

    for i in range(len(num_str)):
        pad.addch(row*2+1, col*5+1+i, num_str[i], curses.color_pair(num_color))


def ColoringTiles(row, col, board, pad):
    tile_num = board.tiles[row][col]
    num_color = 0
    num_color_map = {2**i: i for i in range(1, 8)}

    if tile_num <= 128 and tile_num > 0:
        num_color = num_color_map[tile_num]
    else:
        num_color = 5

    DrawingNumber(row, col, board, pad, num_color)
    if col < (board.size() - 1):
        pad.addch(row*2+1, (col+1)*5, '|')
    if row < (board.size() - 1):
        pad.addstr(row*2+2, col*5+1, '-'*4)
        if col < (board.size() - 1):
            pad.addch(row*2+2, (col+1)*5, '+')
