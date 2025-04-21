# 1244

import sys

input = sys.stdin.readline

N = int(input())
s = input().split
student = int(input())

for _ in range(student):
    g, su = map(int,input().split())


if g == 1:
    for i in range(N):
        if i % su == 0:
            if s[i] == 0:
                1
            else:
                0
else:
    for j in range(N):
        if s[su-j] == s[su+j]:
            if s[su-j] == 0:
                1
            elif s[su-j] == 1:
                0
            elif s[su] == 1:
                0
            elif s[su] == 0:
                1
            elif s[su+j] == 1:
                0
            elif s[su+j] == 0:
                1
        else:
            if s[su] == 1:
                0
            elif s[su] == 0:
                1




# n = int(input())
# switches = list(map(int, input().split()))
# students = int(input())

# for _ in range(students):
#     gender, num = map(int, input().split())
#     if gender == 1:  # 남학생
#         for i in range(num - 1, n, num):
#             switches[i] = 1 - switches[i]
#     else:  # 여학생
#         idx = num - 1
#         left = right = idx
#         while left >= 0 and right < n and switches[left] == switches[right]:
#             left -= 1
#             right += 1
#         for i in range(left + 1, right):
#             switches[i] = 1 - switches[i]

# for i in range(n):
#     print(switches[i], end=' ')
#     if (i + 1) % 20 == 0:
#         print()
