"""
this solution is not O(log(n+m))
I have to change this logic as O(log(n+m)).
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        result = result + nums1[i:] + nums2[j:]
        size = len(result)
        return (result[size//2]) if size % 2 != 0 else (result[size//2 - 1] + result[(size//2)])/2