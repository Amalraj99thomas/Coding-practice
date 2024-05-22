from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
        
#Testrun:
    
nums = [-4,-1,-1,0, 1, 2] 

# nums = [2,7,11,15]
# target = 9


sol_ins = Solution()

result = sol_ins.threeSum(nums)

print(result)