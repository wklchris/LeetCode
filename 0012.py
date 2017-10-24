'''
12. Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Note by wklchris:

    1 5 10 50 100 500 1000
    I V X  L  C   D   M

'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
             (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        s = ''
        while num > 0:
            for j, ch in d:
                while num >= j:
                    s += ch
                    num -= j
        return s


# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().intToRoman
        test_case = [4, 7, 8, 54, 3900]
        test_answer = ["IV", "VII", "VIII", "LIV", "MMMCM"]

        for i, j in zip(test_case, test_answer):
            self.assertEqual(func(i), j)


if __name__ == "__main__":
    unittest.main()
