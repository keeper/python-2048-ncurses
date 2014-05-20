import random


class Board:
    def __init__(self, size):
        self.tiles = [[0] * size for i in range(0, size)]
        self.NewTile()
        self.NewTile()
        self.score = 0

    def __repr__(self):
        content = ""
        for row in self.tiles:
            for col in row:
                content += str(col)
            content += "\n"
        return content

    def __str__(self):
        content = ""
        for row in self.tiles:
            for col in row:
                content += str(col)
            content += "\n"
        return content

    def __getitem__(self, index):
        return self.tiles[index]

    def empty_pos(self):
        empty_pos_list = []
        for row_idx in range(0, len(self.tiles)):
            for col_idx in range(0, len(self.tiles)):
                if self.tiles[row_idx][col_idx] == 0:
                    empty_pos_list.append((row_idx, col_idx))
        return empty_pos_list

    def NewTile(self):
        empty_pos_list = self.empty_pos()
        if empty_pos_list == []:
            return
        random.shuffle(empty_pos_list)
        new_pos_x, new_pos_y = empty_pos_list[0][0], empty_pos_list[0][1]
        self.tiles[new_pos_x][new_pos_y] = 2 ** random.randint(1, 2)

    def size(self):
        return len(self.tiles)

    def is_full(self):
        return len(self.empty_pos()) == 0

    def MoveUp(self):
        # rotate 90 degree clock-wise
        # then call MoveRight
        rotate_cw(self.tiles)
        moved = self.MoveRight()
        # then rotate ccw back
        rotate_ccw(self.tiles)
        return moved

    def MoveDown(self):
        # rotate 90 degree clock-wise
        # then call MoveLeft
        rotate_cw(self.tiles)
        moved = self.MoveLeft()
        # then rotate ccw back
        rotate_ccw(self.tiles)
        return moved

    def MoveLeft(self):
        orig_size = self.size()
        moved = False
        for row_idx in range(len(self.tiles)):
            orig_row = list(self.tiles[row_idx])
            row = self.tiles[row_idx]
            row = [val for val in row if val != 0]
            for i in range(len(row)-1):
                if row[i] == row[i+1]:
                    row[i] += row[i+1]
                    row[i+1] = 0
                    self.score += row[i]
            row = [val for val in row if val != 0]
            for i in range(len(row), orig_size):
                row.append(0)
            self.tiles[row_idx] = row
            if row != orig_row:
                moved = True
                self.NewTile()
        return moved

    def MoveRight(self):
        # reverse the row
        # then call MoveLeft
        for row in self.tiles:
            row = row.reverse()
        moved = self.MoveLeft()
        # reverse back
        for row in self.tiles:
            row = row.reverse()
        return moved

    def GameOver(self):
        size = len(self.tiles)
        for i in range(size):
            for j in range(size):
                cur_tile = self.tiles[i][j]
                if i != 0:
                    if cur_tile == self.tiles[i-1][j]:
                        return False
                if i < size - 1:
                    if cur_tile == self.tiles[i+1][j]:
                        return False
                if j != 0:
                    if cur_tile == self.tiles[i][j-1]:
                        return False
                if j < size - 1:
                    if cur_tile == self.tiles[i][j+1]:
                        return False
        return True


def rotate_cw(tiles):
    rotated = zip(*tiles[::-1])
    for row_idx in range(len(tiles)):
        tiles[row_idx] = list(rotated[row_idx])


def rotate_ccw(tiles):
    rotated = zip(*tiles)[::-1]
    for row_idx in range(len(tiles)):
        tiles[row_idx] = list(rotated[row_idx])


if __name__ == "__main__":
    board = Board(2)
    for i in range(4):
        board.NewTile()
    print board
    board.MoveDown()
    board.MoveDown()
    board.MoveDown()
    board.MoveDown()
    board.MoveDown()
    print board
