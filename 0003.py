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
        for i in range(len(s)):
            if s[i] in d:
                L = max(L, i - head)
                head = max(head, d[s[i]] + 1)
            d[s[i]] = i
        L = max(L, len(s) - head)

        return L


# TEST ONLY
if __name__ == "__main__":
    from _mytest import timetest

    timetest(Solution().lengthOfLongestSubstring, "pwwkew")