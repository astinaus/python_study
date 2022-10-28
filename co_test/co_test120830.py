def solution(n, k):

    a = n * 12000
    b = k * 2000
    c = n // 10 * 2000

    return a + b - c

print(solution(64, 6))