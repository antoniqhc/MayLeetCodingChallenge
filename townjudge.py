class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        hshmp = {n:[0,True] for n in range(1,N+1)}
        
        for item in trust:
            hshmp[item[1]][0] += 1
            hshmp[item[0]][1] = False

        for key in hshmp.keys():
            if hshmp[key][0] == N-1 and hshmp[key][1]:
                return key
            
        
        return -1