/*
 NOTE:: https://leetcode.com/problems/add-two-numbers/description/
 */

/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun ListNode?.value() = this?.`val` ?: 0

    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        val head = ListNode(0)
        var cur = head
        var carry = 0
        var n1 = l1
        var n2 = l2

        while (n1 != null || n2 != null) {
            val sum = n1.value() + n2.value() + carry
            cur.next = ListNode(sum % 10)
            cur = cur.next

            carry = if (sum > 9) 1 else 0
            if (n1 != null) n1 = n1.next
            if (n2 != null) n2 = n2.next


        }

        if (carry > 0) {
            cur.next = ListNode(carry)
            cur = cur.next
        }

        return head?.next
    }
}
