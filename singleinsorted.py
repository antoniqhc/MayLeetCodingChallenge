class Solution(object):
    def recurseNonDup(self, nums):
        print(nums)
        if len(nums) <= 3:
            d = {i:0 for i in nums}
            for i in nums:
                d[i] += 1
                
            for key in d.keys():
                if d[key] == 1:
                    return key
        
        mid = (len(nums)//2)
        if mid % 2 == 0:
            if nums[mid] == nums[mid+1]:
                # target is after mid
                return self.recurseNonDup(nums[mid:])
            else:
                # target is before mid
                return self.recurseNonDup(nums[:mid+1])
                
        else:
            if nums[mid] == nums[mid-1]:
                # target is after mid
                return self.recurseNonDup(nums[mid-1:])
            else:
                # target is before mid
                return self.recurseNonDup(nums[:mid])
        
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return self.recurseNonDup(nums)