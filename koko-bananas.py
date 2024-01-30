from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles : List[int], h : int) -> int:
        
        l = round(sum(piles)/h)  # min value for speed. ME ADD!
        r =  max(piles)
        speed = r

        while l <= r:
            k = l + ((r - l)//2)
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / k)

            if hrs <= h:
                speed = min(speed, k)
                r = k - 1
            else:
                l = k + 1
        return speed


#Testrun
    
soin = Solution()

piles = [30,11,23,4,20]
h = 5

result = soin.minEatingSpeed(piles, h)
print(result)