class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maximum = 0
        for i in nums:
            if i==1:
                current +=1
                maximum = max(current, maximum)
            else:
                current =0

        return maximum