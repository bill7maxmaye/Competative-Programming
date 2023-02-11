class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        for num in counter:
            if counter.get(k-num, 0):
                if num != k - num:
                    res += min(counter[num], counter[k-num])
                    counter[k-num] = 0
                    counter[num] = 0
                else:
                    res += int(counter[num] / 2)

        return res
