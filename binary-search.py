from typing import List
class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int] # nums is sorted ascending
        :type target: int
        :rtype: int
        """
        #define pointers
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
    

#Test:
    
nums = [-1,0,3,4,4,5,9,12] 
target = 6

sol_ins = Solution()

result = sol_ins.search(nums, target)

print(result)
