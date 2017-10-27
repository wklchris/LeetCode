'''
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]  # Only one
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lst, i = [], 0
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if s < 0:
                        j += 1
                    elif s > 0:
                        k -= 1
                    else:
                        lst.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1

        return lst

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().threeSum
        self.assertEqual(func([-1,0,1,2,-1,-4]), [(-1, -1, 2), (-1, 0, 1)])

if __name__ == "__main__":
    unittest.main()