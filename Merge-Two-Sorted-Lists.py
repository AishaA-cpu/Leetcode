# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # one list is longer than the other
        # two nodes are of equal value
        # both lists are empty
        res = None
       
        if not list1 or not list2:
            return list2 if not list1 else list1
        
        curr, temp, res = None, None, None
       
        curr, temp = (list1, list2) if list1.val <= list2.val else (list2, list1)
    
        res = curr
        while curr.next and temp:
            if curr.next.val <= temp.val:
                curr = curr.next
            else:
                temp2 = curr.next
                curr.next = temp
                temp = temp2
                curr = curr.next
        if temp is not None:
            curr.next = temp
        
        return res




         