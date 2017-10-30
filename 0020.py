'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n % 2 > 0:
            return False
        d = {"(": ")", "{": "}", "[": "]"}
        lst = []
        for ch in s:
            if ch in d:
                lst.append(ch)
            elif not lst or d[lst[-1]] != ch:
                return False
            else:
                lst.pop()
        return False if lst else True

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().isValid
        self.assertEqual(func("()"), True)
        self.assertEqual(func("})"), False)
        self.assertEqual(func("(]"), False)
        self.assertEqual(func("({[]()})"), True)

if __name__ == "__main__":
    unittest.main()