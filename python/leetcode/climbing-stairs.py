class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prev_prev = 0
        for i in range(n):
            fibo = prev + prev_prev
            prev_prev, prev = prev, fibo
        return prev