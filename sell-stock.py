from typing import List
class solution():
    def sellstock(self,prices : List[int]):

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # new lowest price found
                l = r
            r += 1
        return maxP
    
# testing
    
#prices = [3,4,2,1]
prices = [4, 2, 3, 1, 5, 6, 7]

soins = solution().sellstock

result = soins(prices)

print(result)