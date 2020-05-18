class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False
        
        window_size = len(s1)
        s1_turing = {chr(i):0 for i in range(97, 123)}
        s2_turing = {chr(i):0 for i in range(97, 123)}
        
        s1_list = list(s1)
        s2_list = list(s2)
        
        for i in range(window_size):
            s1_turing[s1_list[i]] += 1
            s2_turing[s2_list[i]] += 1
            
        if s1_turing == s2_turing:
                return True
            
        for i in range(window_size, len(s2)):
            s2_turing[s2_list[i]] += 1
            s2_turing[s2_list[i-window_size]] -= 1
            
            if s1_turing == s2_turing:
                return True
            
        return False