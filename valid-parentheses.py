class Solution:
    def validparent(self, s: str) -> bool:
        stack = []
        # hashmap where the closing parentheses is the key
        closeToOpen = { "]" : "[" , ")" : "(" , "}" : "{" }

        for c in s:
            if c in closeToOpen:
            # if c is closing parentheses:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  #remove the pair of parentheses
                else:
                    return False
            # if c is opening parentheses 
            else:
                stack.append(c)

        return True if not stack else False


s = "()"

sol_inc = Solution()

result = sol_inc.validparent(s)

print(result)
