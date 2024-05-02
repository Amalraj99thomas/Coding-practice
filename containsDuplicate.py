from typing import List
class Solution(object):
    def contains_duplicate(self, nums : List[int]) -> bool:
        user_array = set() #hashset

        for n in nums:
            if n in user_array:
                return True
            user_array.add(n)
        return False # loop exits as all elements are distinct
    

nums = [1, 2, 3, 4, 5, 6]

solution_instance = Solution()

result = solution_instance.contains_duplicate(nums)

print(result)
