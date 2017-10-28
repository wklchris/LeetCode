'''
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

1:N/A,  2:abc, 3:def,
4:ghi,  5:jkl, 6:mno,
7:pqrs, 8:tuv, 9:wxyz,
        0:N/A

    Input:Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]. 

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

wklchris Note:
0 or 1 will NOT be present in the input. In case they do, use 1="*" and 0=" ". 
'''

from functools import reduce
class Solution:
    def letterCombinations(self, digits):
        if '' == digits: return []
        d = {'2': 'abc', '3': 'def',
             '4': 'ghi', '5': 'jkl', '6': 'mno',
             '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return reduce(lambda x, y: [i + j for i in x for j in d[y]], digits, [''])


# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().letterCombinations
        self.assertEqual(func("23"), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])

if __name__ == "__main__":
    unittest.main()
