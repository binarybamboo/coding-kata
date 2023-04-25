"""
link: https://school.programmers.co.kr/learn/courses/30/lessons/92335?itm_content=course14743

"""
import math


def convert_k_decimal_point(n, k):
    result = ''

    if k == 10:
        return n

    while n:
        result += str(n % k)
        n = n // k
    return result[::-1]


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    # STEP 1: convert to n as k decimal point
    converted_n = convert_k_decimal_point(n, k)

    result = 0
    # STEP 2: count all prime that matched the conditions
    for n in converted_n.split('0'):
        if n == "": continue
        if is_prime(int(n)):  # n이 소수인 경우 answer+=1
            result += 1
    return result


print(solution(437674, 3))
