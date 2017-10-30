'''
21. Merge Two Sorted List


'''
# Definition for singly-linked list.
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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        linklst = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return linklst.next

