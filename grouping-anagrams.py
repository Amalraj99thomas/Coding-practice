from collections import defaultdict
from typing import List
class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26 # for 26 alphabets

            for c in word:
                count[ord(c) - ord('a')] +=1 # find index of c in 26 alphabets and add 1 to it

            key = tuple(count)
            anagrams_dict[key].append(word) #defaultdict checks if key exists

        return anagrams_dict.values()
    
# Test input
#strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["a"]

# Create an instance of the Solution class
solution_instance = Solution()

# Call the groupAnagrams method with the test input
result = solution_instance.groupAnagrams(strs)

# Print the result
print(result)

