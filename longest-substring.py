class Solution:
    def lenLongestSubstring(self, s : str) -> int:
        charset = set() # window containing characters
        l = 0
        maxlen = 0

        for r in range(len(s)):
            # if s[r] char is already in the set
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            # if s[r] not in set, add
            charset.add(s[r])
            #compute len after adding char
            maxlen = max(maxlen, r - l + 1)
            # r++
        return maxlen
    
#testrun
    
sol = Solution()

string = 'pwwkew'

result = sol.lenLongestSubstring(string)

print(result)