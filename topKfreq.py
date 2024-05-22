from typing import List
class solution:
    def topKfreq(self, nums: List[int], k: int) -> List[int]:

        #hashmap
        count = {}
        #List of lists
        freq = [[] for i in range(len(nums) + 1)]

        # count occurances in hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0) # default value 0 
        # store occurances in freq
        for n, c  in count.items():
            freq[c].append(n)

        res = []
        #iterate through freq in reverse order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        