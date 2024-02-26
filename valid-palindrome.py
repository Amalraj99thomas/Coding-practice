class Solution:
    def alphanum(self, c):
        """
        returns true if c is an alphabetic letter (A/a) or a digit
        """
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
    def isPalindrome(self, s: str)->bool:
        """
        :type s: str
        :rtype: bool
        """
        #initializing pointers
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1 # increment pointer if val at l is not alpha numeric
            while l < r and not self.alphanum(s[r]):
                r -= 1
            #comparing left and right pointer values
            if l>r or s[l].lower() != s[r].lower():
                # print('hey')
                return False
            else:
                # print('oh')
                l, r = l + 1, r - 1 # shift pointer to the next val
        return True



strs = 'R!ace&car'

# Create an instance of the Solution class
solution_instance = Solution()

# Call the groupAnagrams method with the test input
result = solution_instance.isPalindrome(strs)

# Print the result
print(result)