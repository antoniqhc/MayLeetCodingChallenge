"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        chars = {}
        
        for char in s:
            if chars.get(char):
                chars[char] += 1
            else:
                chars[char] = 1
            
        ch = []
        for key, val in chars.items():
            if val != 0:
                ptr = 0
                while ptr < len(ch) and ch[ptr][0] > val:
                    ptr += 1
                
                ch.insert(ptr, [val, key])
                
        ans = ''
        
        for el in ch:
            ans += el[1]*el[0]
            
        return ans