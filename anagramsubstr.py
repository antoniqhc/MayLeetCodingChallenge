class ContinueI(Exception):
    pass
    
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        solution = []
        continue_i = ContinueI()
        prev_anagram = False
        window_size = len(p)
        list_p = list(p)
        set_p = set(list_p)
        turing_og = {chr(u):0 for u in range(97, 123)}
        
        for k in range(0,len(list_p)):
            turing_og[list_p[k]] -= 1
            
        i = 0
        while i <= len(s)-window_size:
            if prev_anagram and len(s) > i+window_size:
                if s[i-1] == s[i+window_size-1]:
                    prev_anagram = True
                    solution.append(i)
                    i += 1
                    continue
                
            substr = list(s[i:i+window_size])
            turing = dict(turing_og)
            for k in range(0,len(substr)):
                turing[substr[k]] += 1

            st = set(turing.values())
            
            try:
                for k in st:
                    if k != 0:
                        raise continue_i
            except ContinueI:
                prev_anagram = False
                if i+window_size < len(s) and s[i+window_size-1] not in set_p:
                    i += window_size
                else:
                    i += 1
                continue
                
            prev_anagram = True
            solution.append(i)
            i += 1
                
        return solution