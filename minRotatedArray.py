from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r: 
            if nums[l] < nums[r]: #already sorted
                res = min(res, nums[l])
                break

            # if not perform BS
            m = (l + r) // 2
            res = min(res, nums[m]) # update res
            if nums[m] > nums[l]: # search right
                l = m + 1
            else:
                r = m - 1
        return res
