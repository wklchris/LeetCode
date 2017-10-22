'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    # TEST ONLY
    def __repr__(self):
        s = [self.val]
        while self.next:
            s.append(self.next.val)
            self = self.next
        return "->".join(str(i) for i in s)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lsum = current = ListNode(0)
        num =  0
        while l1 or l2 or num:
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            current.next = ListNode(num % 10)
            current = current.next
            num //= 10

        return str(lsum.next)


# TEST ONLY
import unittest

class TestConvert(unittest.TestCase):
    def test_equal(self):
        func = Solution().addTwoNumbers
        a, a.next = ListNode(2), ListNode(4)
        b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(9)

        self.assertEqual(func(a, b), "7->0->0->1")


if __name__ == "__main__":
    unittest.main()

