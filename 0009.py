'''
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

 |  Some hints:
 |  Could negative integers be palindromes? (ie, -1)
 |
 |  If you are thinking of converting the integer to string, note the restriction of using extra space.
 |
 |  You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
 |  you know that the reversed integer might overflow. How would you handle such case?
 |
 |  There is a more generic way of solving this problem.
 |__
'''
class Solution:
    #
    # Total 2 approaches are introduced.
    #
    # First approach: O(1) space. O(n) time cxty.
    #
    def isPalindrome(self, x):
        if x < 0:
            return False
        r = 1
        while x / r >= 10:
            r *= 10
        while r > 1:
            left, x =divmod(x, r)
            x, right = divmod(x, 10)
            if left != right:
                return False
            r //= 100
        return True
    #
    # Second approach: num2str function.
    #
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x == x[::-1]:  # It should be O(n) Time Cxty
            return True
        else:
            return False

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().isPalindrome
        self.assertEqual(func(121), True)
        self.assertEqual(func(1), True)
        self.assertEqual(func(2332), True)
    
    def test_equal2(self):
        func = Solution().isPalindrome2
        self.assertEqual(func(121), True)
        self.assertEqual(func(1), True)
        self.assertEqual(func(2332), True)

if __name__ == "__main__":
    unittest.main()
