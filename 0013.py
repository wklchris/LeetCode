'''
13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Note by wklchris:

    1 5 10 50 100 500 1000
    I V X  L  C   D   M

'''
import functools

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        numlst = [-d[s[i]] if d[s[i]] < d[s[i + 1]] else d[s[i]] for i in range(len(s)-1)]
        return sum(numlst) + d[s[-1]]
    

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().romanToInt
        test_case = ["IV", "VII", "VIII", "LIV", "MMMCM"]
        test_answer = [4, 7, 8, 54, 3900]

        for i, j in zip(test_case, test_answer):
            self.assertEqual(func(i), j)


if __name__ == "__main__":
    unittest.main()
