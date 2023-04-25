"""
link: https://school.programmers.co.kr/learn/courses/30/lessons/42747?itm_content=course14743
"""


def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer = i + 1
    return answer


print(solution([3, 0, 6, 1, 5]) == 3)
