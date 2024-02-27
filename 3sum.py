from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            # not the first element and also not same as the previous element
            if i > 0 and val == nums[i - 1]:
                continue # bypasses the rest of the loop and finds unique val

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]]) 
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res   
    
#Testrun:
    
nums = [-4,-1,-1,0, 1, 2] 

# nums = [2,7,11,15]
# target = 9


sol_ins = Solution()

result = sol_ins.threeSum(nums)

print(result)