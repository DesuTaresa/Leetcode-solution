# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pr= None
        curr = head
        while curr is not None:
            node =curr.next
            curr.next = pr
            pr = curr
            curr = node
        return pr