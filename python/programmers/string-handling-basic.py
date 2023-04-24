"""
link: https://school.programmers.co.kr/learn/courses/30/lessons/12918?itm_content=course14743
"""

""" first try

def isAllNumberChr(s):
    return all([x.isnumeric() for x in s])
def solution(s):
    if len(s) ==4 or len(s) ==6:
        if isAllNumberChr(s):
            return True
    return False
"""

def solution(s):
    if len(s) in [4, 6] and s.isdigit():
        return True
    return False

print(solution("a234")) # False
print(solution("1234")) # True
