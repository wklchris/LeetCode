from functools import reduce
class Solution:
    #
    # Total 2 approaches are intorduced.
    # 
    # Complexity: O(mn), where m is length of the longest common prefix.
    #
    # First: Pythonic golfing.
    #
    def longestCommonPrefix(self, strs):
        s, z = "", zip(*strs)
        # Read strs "matrix" column by column
        for k in z:
            if len(set(k)) > 1:
                break
            s += k[0]
        return s
    #
    # Second: Step-and-Compare.
    #
    def cmpTwoStrs(self, str1, str2):
        i, n = 0, min(len(str1), len(str2))
        while i < n and str1[i] == str2[i]:
            i += 1
        return str1[:i]

    def longestCommonPrefix2(self, strs):
        # from functools import reduce
        return reduce(self.cmpTwoStrs, strs) if strs else ""


# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().longestCommonPrefix
        self.assertEqual(func(["abeyd", "ab", "abc", "abed"]), "ab")
        self.assertEqual(func(["a", "", "ge"]), "")

        func2 = Solution().longestCommonPrefix2
        self.assertEqual(func2(["abeyd", "ab", "abc", "abed"]), "ab")
        self.assertEqual(func2(["a", "", "ge"]), "")        


if __name__ == "__main__":
    unittest.main()
