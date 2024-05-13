from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bad_orange = []
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        height = len(grid)
        width = len(grid[0])
        fresh = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    bad_orange.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1

        ans = -1
        while len(bad_orange) != 0:
            ans += 1
            tmp = [row[:] for row in bad_orange]
            bad_orange = []
            for pos in tmp:
                for d in direction:
                    i = pos[0] + d[0]
                    j = pos[1] + d[1]
                    if 0 <= i < height and 0 <= j < width and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        bad_orange.append([i, j])

        return -1 if fresh > 0 else max(0, ans)
