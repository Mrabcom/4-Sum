
class Solution(object):
    def fourSum(self, nums, target):
        if nums == []:
            return nums
        nums.sort()
        element = []
        wholeSet = []
        Max = max(nums)
        Min = min(nums)
        for A in range(0,len(nums)-3):
            if (nums[A]+(3*Max) < target) or (nums[A]+(3*Min) > target):
                continue
            for B in range(A+1,len(nums)-2):
                if (nums[A]+nums[B]+(2*Max) < target) or (nums[A]+nums[B]+(2*Min) > target):
                    continue
                for C in range(B+1,len(nums)-1):
                    if (nums[A]+nums[B]+nums[C]+Max < target) or (nums[A]+nums[B]+nums[C]+Min > target):
                        continue
                    for D in range(C+1,len(nums)):
                        if (nums[A]+nums[B]+nums[C]+nums[D] == target):
                            element = [nums[A], nums[B], nums[C], nums[D]]
                            if element not in wholeSet:
                                wholeSet.append(element)
                            element = []
                            break
        
        return wholeSet
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
