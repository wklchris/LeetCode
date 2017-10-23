'''
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        v, i, j = 0, 0, len(height) - 1
        while i < j:
            left, right = height[i], height[j]
            h = min(left, right)
            v = max(v, (j - i) * h)
            while height[i] <= h and i < j:
                 i += 1
            while height[j] <= h and j > i:
                j -= 1
        return v

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().maxArea
        self.assertEqual(func([1, 2]), 1)
        self.assertEqual(func([3, 2]), 2)
        self.assertEqual(func([2, 3, 6, 9]), 6)

if __name__ == "__main__":
    unittest.main()
