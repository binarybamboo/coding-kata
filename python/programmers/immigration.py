"""
 link: https://school.programmers.co.kr/learn/courses/30/lessons/43238?itm_content=course14743
"""


def solution(n, times):
    left = min(times)
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2
        spent_time = 0

        for time in times:
            spent_time += mid // time

        if spent_time >= n:
            right = mid
        else:
            left = mid + 1
    return left


print(solution(6, [7, 10]) == 28)

"""
first idea, 
- recursion like DFS
    but It must be timeout. 
    
second idea,
    binary search 
"""
