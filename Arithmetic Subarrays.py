class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        lst=[]
        for i in range(len(l)):
           
            a=nums[l[i]:r[i]+1]
            a.sort()
            x=Solution().check(a)
          
            lst.append(x)
        return lst
        
    def check(self,arr):
        if len(arr)==2:
            return True
        for i in range(1,len(arr)-1):
            if arr[i]-arr[i-1]!=arr[i+1]-arr[i]:
                return False
        return True
