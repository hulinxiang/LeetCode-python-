class Solution:
    def distinctIntegers(self, n: int) -> int:
        ans = 1
        arr = [0] * (n + 1)
        stack = [n]
        while len(stack) != 0:
            x = stack.pop()
            for i in range(1, n + 1):
                if x % i == 1 and arr[i] == 0:
                    arr[i] = 1
                    ans += 1
                    stack.append(i)
        return ans
