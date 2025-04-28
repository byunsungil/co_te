# 19532

# import numpy as np

# n = list(map(int, input().split()))  # 예: 1 2 3 4 5 6

# # 2x2 행렬과 2x1 벡터로 만들기
# a = np.array([[n[0], n[1]],
#               [n[3], n[4]]])

# b = np.array([n[2], n[5]])

# # 연립방정식 풀기
# x = np.linalg.solve(a, b)

# # 출력
# print(*(int(i) for i in x))

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            exit()

