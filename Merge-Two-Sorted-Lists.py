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
        if not list1:
            res = list2
            return res
        if not list2:
            res = list1
            return res
        if list1.val <= list2.val:
            curr = list1
            res = curr
            temp = list2
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
        else:
            curr = list2
            res = curr
            temp = list1
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

         