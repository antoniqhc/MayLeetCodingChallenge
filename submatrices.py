"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1

"""


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        num_squares = 0
        h = len(matrix)
        w = len(matrix[0])
        
        for i in range(h):
            for j in range(w):
                is_square = True
                width = 1
                while is_square:
                    for x in range(0, width):
                        # exit if out of bounds
                        if i+x >= h:
                            is_square = False
                            break 
                        for y in range(0, width):
                            # exit if out of bounds or not a 1
                            if j+y >= w or matrix[i+x][j+y] == 0:
                                is_square = False
                                break
                                
                        if not is_square:
                            break
                                
                    # never exited so, it must be a square
                    if is_square:
                        num_squares += 1
                        width += 1
                        
                    
        return num_squares
        