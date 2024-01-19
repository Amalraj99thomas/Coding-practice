class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        #pointers for storing top and bottom rows
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = top + ((bot - top) // 2)
            if target < matrix[row][0]:
                bot = row - 1 # Go up
            elif target > matrix[row][-1]:
                top = row + 1 # Go down
            else:
                break

        if not (top <= bot):
            return False #target not found
        
        # row = top + ((bot - top) // 2)
        l, r = 0, COLS -1
        while l <= r:
            m = l + (r - l) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
            
        return False

        


#Test:
    
matrix = [[-1,0,3], [4,4,5], [9,12,15]] 
target = 0

sol_ins = Solution()

result = sol_ins.searchMatrix(matrix, target)

print(result)