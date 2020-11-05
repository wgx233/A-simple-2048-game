from random import randint
ROW = COL = 4 # 为了代码实现方便起见(其实是我太懒), 这里ROW = COL, 否则在矩阵旋转的时候会出错
DOWN, RIGHT, UP, LEFT = range(4)

prob = [2] * 9 + [4]  # 使得每次新加的数选中2的概率为9/10, 选中4的概率为1/10

class Game:
    def __init__(self):
        self._grid, self._score = [[0 for i in range(COL)] for j in range(ROW)], 0
        self.ok = True
        self._grid[randint(0, ROW - 1)][randint(0, COL - 1)] = prob[randint(0, 9)]
        self._grid[randint(0, ROW - 1)][randint(0, COL - 1)] = prob[randint(0, 9)]

    def create_tiles(self): # 每次移动完加一个新的数字2或者4
        avail = []
        for i in range(0, ROW):
            for j in range(0, COL):
                if self._grid[i][j] == 0: avail.append((i, j))
        if len(avail) == 0:
            return False
        (i, j) = avail[randint(0, len(avail) - 1)]
        self._grid[i][j] = prob[randint(0, 9)]
        return True

    @staticmethod
    def upsideDown(grid): # 上下翻转
        i, j = 0, ROW - 1
        while i < j:
            grid[i], grid[j] = grid[j], grid[i]
            i, j = i + 1, j - 1

    @staticmethod
    def Rotate(grid, clk = 1): # 旋转90°, clk = 1 顺时针否则逆时针
        if clk == 1:
            grid[:] = map(list, zip(*grid[::-1]))
        else:
            grid[:] = map(list, zip(*grid))
            grid = Game.upsideDown(grid)

    @staticmethod
    def compress(grid): # 往下压缩格子的空隙
        tail = [ROW - 1 + (grid[ROW - 1][i] == 0) for i in range(COL)]
        for i in range(ROW - 2, -1, -1):
            for j in range(0, COL):
                if grid[i][j]:
                    grid[i][j], grid[tail[j] - 1][j] = 0, grid[i][j]
                    tail[j] -= 1

    @staticmethod
    def moveDown(grid): # 向下合并
        Game.compress(grid)
        add = 0
        for i in range(ROW - 2, -1, -1):
            for j in range(0, COL):
                if grid[i][j] and grid[i + 1][j] == grid[i][j]:
                    add += grid[i][j]
                    grid[i][j], grid[i + 1][j] = 0, grid[i][j] * 2
        Game.compress(grid)
        return add

    def Move(self, direction): # 移动
        if not self.ok:
            return False
        grid_cpy = self._grid[:]
        if direction == UP:
            Game.upsideDown(grid_cpy)
            self._score += Game.moveDown(grid_cpy)
            Game.upsideDown(grid_cpy)
        elif direction == DOWN:
            self._score += Game.moveDown(grid_cpy)
        elif direction == LEFT:
            Game.Rotate(grid_cpy, -1)
            self._score += Game.moveDown(grid_cpy)
            Game.Rotate(grid_cpy)
        elif direction == RIGHT:
            Game.Rotate(grid_cpy)
            self._score += Game.moveDown(grid_cpy)
            Game.Rotate(grid_cpy, -1)
        self._grid = grid_cpy
        self.ok = self.create_tiles()
        return self.ok

    def getGrid(self):
        return self._grid[:]

    def getMax(self):
        mx = [max(self._grid[i]) for i in range(ROW)]
        return max(mx)

    def getScore(self):
        return self._score

    def notOver(self):
        return self.ok
