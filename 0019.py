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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        helper = cur = head
        for _ in range(n):
            helper = helper.next
        if not helper:
            return head.next
        while helper.next:
            helper = helper.next
            cur = cur.next
        cur.next = cur.next.next
        return head
