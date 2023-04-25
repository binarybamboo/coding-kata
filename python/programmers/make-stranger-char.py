"""
link: https://school.programmers.co.kr/learn/courses/30/lessons/12930?itm_content=course14743
"""


def solution(s):
    res = []
    for x in s.split(' '):
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word)
    return ' '.join(res)


print(solution("try hello world"))
