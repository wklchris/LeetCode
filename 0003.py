'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        head = L =  0
        for i, t in enumerate(s):
            if t in d:
                L = max(L, i - head)
                head = max(head, d[t] + 1)
            d[t] = i

        return max(L, len(s) - head)


# TEST ONLY
if __name__ == "__main__":
    from _mytest import timetest

    timetest(Solution().lengthOfLongestSubstring, "pwwkew")