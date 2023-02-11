class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(1, n):
            best = -math.inf
            for j in range(max(i-k, 0), i):
                best = max(best, nums[j] + nums[i])
            nums[i] = best
        return nums[n-1]
