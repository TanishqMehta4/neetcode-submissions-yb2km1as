# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        count  = 0 

        temp = prev
        prev = cur
        cur = temp

        while cur:
            if count == n-1:
                cur = cur.next

            else:

                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            count += 1

        return prev