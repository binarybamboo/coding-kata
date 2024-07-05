/*
 NOTE:: https://leetcode.com/problems/two-sum/
 */

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val mm = mutableMapOf<Int, Int>()

        for ((i, value) in nums.withIndex()) {
            val diff = target - value
            val subtractedValue = mm.get(diff)

            subtractedValue?.let {
                return intArrayOf(subtractedValue, i)
            }

            mm[value] = i

        }

        return intArrayOf()
    }
}

