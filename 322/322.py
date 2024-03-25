import sys
from typing import List

'''使用动态规划来解题'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化dp, dp[0]肯定
        dp = [0] * (amount + 1)
        # 对金额进行遍历
        for i in range(1, amount + 1):
            min_value = sys.maxsize
            # 对硬币的面值进行遍历
            for coin in coins:
                # i-coin >=0 表示加上一个硬币
                # dp[i-coin]<min_value表示有更优解
                if i - coin >= 0 and dp[i - coin] < min_value:
                    min_value = dp[i - coin] + 1
                dp[i] = min_value

        return dp[amount] if dp[amount] != sys.maxsize else -1


coins = [2]
amount = 3
solution = Solution()
print(solution.coinChange(coins, amount))
