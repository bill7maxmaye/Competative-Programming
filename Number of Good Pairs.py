class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
     
        ans = 0
        l = len(nums)
        for i in range(l):
            for j in range(1,l):
                if nums[i] == nums[j] and i < j:
                    ans += 1
        return ans
obj = Solution()
print(obj.numIdenticalPairs([1,1,1,1])) 
