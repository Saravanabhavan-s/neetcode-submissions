class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        q = deque()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        visited = set()
        while q:
            r, c, dst = q.popleft()
            for x, y in dirs:
                dx = r + x
                dy = c + y
                if 0 <= dx < row and 0 <= dy < col:
                    if grid[dx][dy] == 2147483647 and (dx, dy) not in visited:
                        grid[dx][dy] = 1 + dst
                        visited.add((dx, dy))
                        q.append((dx, dy, 1 + dst))
