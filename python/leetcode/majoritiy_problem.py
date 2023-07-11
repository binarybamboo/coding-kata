class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major = 0
        for ele in nums:
            if count == 0:
                major = ele
            if major == ele:
                count += 1
            else:
                count -= 1
        return major
