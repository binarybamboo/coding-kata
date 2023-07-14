# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        str_num = ''

        while head:
            str_num = str_num + str(head.val)
            head = head.next

        len_num = len(str_num)

        for i in range(0,len_num//2):
            if str_num[i] != str_num[len_num-1-i]:
                return False
        return True
