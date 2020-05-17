class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        epsilon = coordinates[1][1] - coordinates[0][1]
        delta = coordinates[1][0] - coordinates[0][0]
        if delta == 0:
            x = coordinates[0][0]
            for i in range(len(coordinates)):
                if coordinates[i][0] != x:
                    return False
            return True
        slope = epsilon/delta
        for i in range(2, len(coordinates)):
            epsilon = coordinates[i][1] - coordinates[i-1][1]
            delta = coordinates[i][0] - coordinates[i-1][0]
            if delta == 0:
                return False
            slope_new = epsilon/delta 
            if slope_new != slope:
                return False
            
        return True