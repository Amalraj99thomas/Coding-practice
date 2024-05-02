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
    
    def longestsubstring(self, st : str) -> int:

        # variables required
        window = set()
        len = 0 
        p = 0 # window pusher

        # c for each character in s 
        for c in range(len(st)):
            # if c in the window
            while st[c] in window:
                window.remove(st[p])
                p += 1
            # if c not in the window, add
            window.add(st[c])
            #calculate max len
            len = max(len, c - p + 1)
        return len






#testrun
    
sol = Solution()

string = 'pwwkepw'

result = sol.longestsubstring(string)

print(result)