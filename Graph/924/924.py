import collections
from typing import List


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        # 首先创建一个ids，表示每个节点属于哪一个类
        n = len(graph)
        ids = [0] * n
        index_size = {}
        cur_id = 0
        for i in range(n):
            if ids[i] == 0:  # 说明当前节点还不属于现在任何的连通分量
                cur_id += 1
                ids[i] = cur_id  # 现在这个节点属于第 cur_id个连通分量
                size = 1
                queue = collections.deque([i]) # 将当前节点压入栈,以便于深度遍历
                while len(queue) != 0:
                    cur = queue.popleft()
                    for j in range(n):
                        if graph[cur][j] == 1 and ids[j] == 0:
                            ids[cur] = cur_id
                            size += 1
                            queue.append(j)

                index_size[cur_id] = size

        # 到这里深度遍历就已经完成了
        idToInitials = {}
        for value in initial:
            idToInitials[ids[value]] = idToInitials.get(ids[value], 0) + 1

        ans = n+1
        ans_remove = 0

        for value in initial:
            remove = index_size[ids[value]] if idToInitials[ids[value]] == 1 else 0
            if remove > ans_remove or (remove == ans_remove and value < ans):
                ans_remove = remove
                ans = value

        return ans
