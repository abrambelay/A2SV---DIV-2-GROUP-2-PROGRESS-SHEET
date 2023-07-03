class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currS = 0
        l = 0
        r = k
        for i in range(k):
            currS+=nums[i]
        maxS = currS
        for i in range(k,len(nums)):
            currS+=nums[r]
            currS-=nums[l]
            r+=1
            l+=1
            maxS = max(maxS,currS)
        return maxS/k
