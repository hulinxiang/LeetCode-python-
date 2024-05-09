from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        # 反向构建邻接表
        for e in edges:
            g[e[1]].append(e[0])

        def dfs(x: int) -> None:
            visit[x] = True  # 代表访问了这个节点
            for y in g[x]:
                if not visit[y]:
                    visit[y] = True
                    dfs(y)

        ans = [None] * n
        for i in range(n):
            visit = [False] * n
            dfs(i)
            visit[i] = False
            ans[i] = [j for j, b in enumerate(visit) if b]

        return ans
