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
        new_tile_pos = empty_pos_list[0]
        self.tiles[new_tile_pos[0]][new_tile_pos[1]] = 2 ** random.randint(1, 2)


    def size(self):
        return len(self.tiles)


    def is_full(self):
        return len(self.empty_pos()) == 0


if __name__ == "__main__":
    board = Board(2)
    for i in range(2):
        board.NewTile()
    print board
    print board.empty_pos()
    print board.is_full()
