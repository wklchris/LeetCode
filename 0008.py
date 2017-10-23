'''
8. String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. 
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). 
You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. 
If you still see your function signature accepts a const char * argument, 
please click the reload button to reset your code definition.

spoilers alert... click to show requirements for atoi.
  |
  |  Requirements for atoi:
  |  The function first discards as many whitespace characters as necessary until the first non-whitespace 
  |  character is found. Then, starting from this character, takes an optional initial plus or minus sign 
  |  followed by as many numerical digits as possible, and interprets them as a numerical value.
  |
  |  The string can contain additional characters after those that form the integral number, which are ignored 
  |  and have no effect on the behavior of this function.
  |
  |  If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such 
  |  sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
  |
  |  If no valid conversion could be performed, a zero value is returned. If the correct value is out of 
  |  the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
  |__
'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # Spaces & Null case
        str = str.strip()
        if len(str) == 0:
            return 0
        
        # Check first digit
        if str[0].isdigit():
            i, sign = 0, True
        elif str[0] == "-":
            i, sign = 1, False
        elif str[0] == "+":
            i, sign = 1, True
        else:
            return 0
        
        # Main Conversion. Break when meet unexpected char
        #   such as ".", " ", etc.
        n = 0
        while i < len(str) and str[i].isdigit():
            n = n * 10 + ord(str[i]) - 48  # ord("0") = 48
            i += 1
        
        # Sign & Integer Overflow
        n = min(n, 2 ** 31 - 1) if sign else max(-n, - 2 ** 31)

        return n


# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().myAtoi
        self.assertEqual(func("12"), 12)
        self.assertEqual(func("-312"), -312)
        self.assertEqual(func("+255"), 255)
        self.assertEqual(func(""), 0)
        self.assertEqual(func("0215"), 215)
        self.assertEqual(func("1.7"), 1)
        self.assertEqual(func(" b11228552307"), 0)
        self.assertEqual(func("2147483648"), 2147483647)
        self.assertEqual(func("-3 2"), -3)

if __name__ == "__main__":
    unittest.main()
