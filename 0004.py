'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

    Input: "babad"

    Output: "bab"

Note: "aba" is also a valid answer.
Example:

    Input: "cbbd"

    Output: "bb"
_'''

class Solution(object):
    #
    # Total 2 approaches introduced here.
    #
    # First Approach: Manacher's Algorithm. O(n).
    #
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s
        
        s = "#" + "#".join(s) + "#"
        p = [0] * len(s)
        center, redge = 0, 0
        max_c = 0
        for i in range(len(s)):
            j = 2 * center - i
            p[i] = min(redge - i, p[j]) if redge > i and j >= 0 else 0
            while i + p[i] + 1 < len(s) and i > p[i] and s[i + p[i] + 1] == s[i - p[i] - 1]:
                p[i] += 1
            if i + p[i] > redge:
                center, redge = i, p[i]
            if p[i] > p[max_c]:
                max_c = i
        lpstr = s[max_c - p[max_c]:max_c + p[max_c]+1].strip("#")

        return lpstr[::2]
    
    #
    # Second approach: a naive thought. O(n^2).
    #
    def findAroundCenter(self, ss, left, right):
        i, j = left, right
        while i >= 0 and j < len(ss) and ss[i] == ss[j]:
            i -= 1
            j += 1
        return j - i - 1
            
    def longestPalindrome2(self, s):
        i, j = 0, 0
        for k in range(len(s)):
            l1 = self.findAroundCenter(s, k, k)
            l2 = self.findAroundCenter(s, k, k + 1)
            lp = max(l1, l2)
            if lp > j - i:
                i = k - (lp - 1) // 2
                j = k + lp // 2
        return s[i:j+1]


# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().longestPalindrome
        func2 = Solution().longestPalindrome2
        test_case = ["abb", "ddc", "abccbda", "a", "", "acdbe"]
        test_answer = ["bb", "dd", "bccb", "a", "", "a"]

        for i, j in zip(test_case, test_answer):
            self.assertEqual(func(i), j)
            self.assertEqual(func2(i), j)

if __name__ == "__main__":
    unittest.main()
