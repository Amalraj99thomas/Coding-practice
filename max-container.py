from typing import List
class Solution():
    # Brute force approach 
    # Time complexity O(n*2)
    def maxContainerBrute(self, height : List[int]) -> int:

        max_area = 0

        for l in range(len(height)):
            for r in range (l + 1, len(height)):
                width = r - l
                ht = min(height[l], height[r])
                area = ht * width
                max_area = max(max_area, area)
        return max_area

    # OPtimized approach 
    # Time complexity O(n)
    def maxContainerOptim(self, height : List[int]) -> int:

        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            ht = min(height[l], height[r])
            width = r - l
            area = ht * width
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1 #maximize area
            else:
                r -= 1

        return max_area


# Testing

height = [1,8,6,2,5,4,8,3,7]

sol_int = Solution()
result = sol_int.maxContainerOptim(height)
print(result)

