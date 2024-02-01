from typing import List
class Solution:
    def twoSum(self, nums : List[int], target : int) -> int:
        l, r = 0, len(nums) - 1

        # assuming nums is sorted and there is one exact solution
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
         
#Testrun:
    
nums = [-1,0] 
target = -1

# nums = [2,7,11,15]
# target = 9


sol_ins = Solution()

result = sol_ins.twoSum(nums, target)

print(result)
        