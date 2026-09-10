# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative method, more optimised
        prev=None
        curr=head
        while curr:
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        return prev