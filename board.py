import random


class Board:
    def __init__(self, size):
        self.tiles = [[0] * size for i in range(0, size)]
        self.NewTile()
        self.NewTile()

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
        pass

    def MoveDown(self):
        pass

    def MoveLeft(self):
        for row in self.tiles:
            del row[0]
            row.append(0)
        pass

    def MoveRight(self):
        pass


if __name__ == "__main__":
    board = Board(2)
    for i in range(2):
        board.NewTile()
    print board
    print board.empty_pos()
    print board.is_full()
    print board[0][1]
