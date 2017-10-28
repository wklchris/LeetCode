'''
18. 4 Sum
'''
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums, target, N, h, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  
                return
            if N == 2: 
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        results.append(h + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or nums[i-1] != nums[i]:
                        findNsum(nums[i+1:], target-nums[i], N-1, h+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().fourSum
        self.assertEqual(func([1, 0, -1, 0, -2, 2], 0), 
                         [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

if __name__ == "__main__":
    unittest.main()
