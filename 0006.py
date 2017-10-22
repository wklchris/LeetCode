'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"

* Note by wklchris: *

    For numRows = 4, the result pattern should be:

    P     I     N
    A   L S   I G
    Y A   H R
    P     I
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        strRow = [""] * len(s)
        i, step = 0, (numRows == 1) -1
        for ch in s:
            strRow[i] += ch
            if i == 0 or i == numRows - 1:
                step = -step
            i += step
        return "".join(strRow)

# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().convert
        self.assertEqual(func("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(func("ABC", 2), "ACB")
        self.assertEqual(func("ABC", 1), "ABC")

if __name__ == "__main__":
    unittest.main()
