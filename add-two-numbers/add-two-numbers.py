# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        totalSum = ListNode()
        carry = 0
        
        temp = totalSum
        while l1 or l2 or carry == 1:
            sum = carry
            if l1 and l2:
                sum += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum += l1.val
                l1 = l1.next
            elif l2:
                sum += l2.val
                l2 = l2.next            
                
            carry = 0
            if sum > 9:
                carry = 1
                sum -= 10

            temp.next = ListNode(sum, None)
            temp = temp.next
                
        return totalSum.next

# time: O(max(m,n))
# space: O(max(m,n))