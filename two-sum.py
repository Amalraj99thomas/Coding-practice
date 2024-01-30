from typing import List
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}  #val : index
        
        # List = [1, 3, 4, 8]

        # 1: 0
        # 3: 1
        # 4: 2
        # 8: 3

        for i, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return(prevMap[diff], i)
            prevMap[val] = i  #if val not found append to preMap


#Test:
    
nums = [1,0,3,4,5,12] 
target = 9

sol_ins = Solution()

result = sol_ins.twoSum(nums, target)

print(result)
        