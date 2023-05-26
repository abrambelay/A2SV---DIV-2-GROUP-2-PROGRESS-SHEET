class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = [0]*3
        for n in nums:
            freq[n]+=1
        i  = 0
        for indx,num in enumerate(freq):
            while num!=0:
                nums[i] = indx
                i+=1
                num-=1
        return nums
