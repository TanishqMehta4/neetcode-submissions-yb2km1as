# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        head1 = l1
        head2 = l2

        count = 0

        while head1 or head2 or count:

            v1 = head1.val if head1 else 0
            v2 = head2.val if head2 else 0

            val = v1 + v2 + count
            count = val//10

            head.next = ListNode(val%10)
            
            head = head.next
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

        
        return dummy.next
