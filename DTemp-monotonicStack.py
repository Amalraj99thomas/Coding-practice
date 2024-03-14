from typing import List
class Solution():
    def dailyTemperature(self, temperatures : List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair : [temp: index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # stack[-1][0] will give the last temp val
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append([t,i])
        return res
