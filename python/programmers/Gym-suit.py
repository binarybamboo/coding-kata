"""
link: https://school.programmers.co.kr/learn/courses/30/lessons/42862?itm_content=course14743

"""


def solution(n, lost, reserve):
    lost_students = set(lost) - set(reserve)
    has_extra = set(reserve) - set(lost)

    lost_students = list(lost_students)
    has_extra = list(has_extra)
    has_extra.sort();
    lost_students.sort()

    for i in lost_students:
        if i - 1 in has_extra:
            has_extra.remove(i - 1)
        elif i + 1 in has_extra:
            has_extra.remove(i + 1)

    return n - len(has_extra)


print(solution(5, [2, 4], [1, 3, 5]) == 5)
print(solution(5, [2, 4], [3]) == 4)
