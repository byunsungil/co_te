# 1929

# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# import sys
# input = sys.stdin.readline

# N, M = map(int,input().split())
# s = []
# for i in range(N,M+1):
#     cnt = 0
#     for j in range(1,M+1):
#         if i % j == 0:
#             cnt += 1
#     if cnt == 2:
#         s.append(i)

# for i in s:
#     print(i)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

for num in range(N, M+1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)