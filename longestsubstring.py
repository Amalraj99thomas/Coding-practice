class Solution:
    def longestsubstring(self, st : str) -> int:

            # variables required
            window = set()
            maxlen = 0 
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
                maxlen = max(maxlen, c - p + 1)
            return maxlen






#testrun
    
sol = Solution()

string = 'pwwkepw'

result = sol.longestsubstring(string)

print(result)