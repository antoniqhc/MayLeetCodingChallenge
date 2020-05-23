"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists
"""


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ptr_A = 0
        ptr_B = 0
        
        intersections = []
        
        while len(A) > ptr_A and len(B) > ptr_B:
            st = None
            end = None
            if A[ptr_A][0] <= B[ptr_B][0] and A[ptr_A][1] >= B[ptr_B][0]:
                st = B[ptr_B][0]
                if A[ptr_A][1] < B[ptr_B][1]:
                    end = A[ptr_A][1]
                    ptr_A += 1
                else:
                    end = B[ptr_B][1]
                    ptr_B += 1
                    
            elif B[ptr_B][0] <= A[ptr_A][0] and B[ptr_B][1] >= A[ptr_A][0]:
                st = A[ptr_A][0]
                if A[ptr_A][1] < B[ptr_B][1]:
                    end = A[ptr_A][1]
                    ptr_A += 1
                else:
                    end = B[ptr_B][1]
                    ptr_B += 1 
                    
            else:
                if A[ptr_A][0] < B[ptr_B][0]:
                    ptr_A += 1
                else:
                    ptr_B += 1 
                    
            if end != None:
                intersections.append([st, end])
                
        return intersections