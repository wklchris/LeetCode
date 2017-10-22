"""
7. Reverse Integer

Reverse digits of an integer.

    Example1: x = 123, return 321
    Example2: x = -123, return -321

click to show spoilers.
  | 
  |  Have you thought about this?
  |  Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
  |
  |  If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
  |
  |  Did you notice that the reversed integer might overflow? 
  |  Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
  |
  |  For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
  |__

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""
class Solution:
    #
    # Total 2 approaches are introduced.
    #
    # First approach: Code-Golf.
    #
    def reverse(self, x):
        s = (x > 0) - (x < 0)  # "sign(x)"
        r = int(str(s * x)[::-1])

        # i.e. "r < 2 ** 31"
        return r * s if r.bit_length() < 32 else 0
    #
    # Second approach: A sound thought.
    #
    def reverse2(self, x):
        s = (x > 0) - (x < 0)
        r, x = 0, s * x
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        
        return r * s if r < 2 ** 31 else 0

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().reverse
        func2 = Solution().reverse2
        
        test_case = [120, -421, 0, 1, 1534236469, -2147483412, -2147483648]
        test_answer = [21, -124, 0, 1, 0, -2143847412, 0]

        for i, j in zip(test_case, test_answer):
            self.assertEqual(func(i), j)
            self.assertEqual(func2(i), j)

if __name__ == "__main__":
    unittest.main()