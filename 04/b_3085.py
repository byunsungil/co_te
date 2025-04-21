# 3085

# 문제
# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

# 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

# 출력
# 첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.


import sys 

input = sys.stdin.readline

N = int(input())

board = [] 

max_count = 0

for _ in range(N):
    c = list(input().strip()) # 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
    board.append(c)


def check(board):
    global max_count
    n = len(board)

    # 행 검사
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_count = max(max_count, cnt)

    # 열 검사
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if board[i][j] == board[i - 1][j]:
                cnt += 1
            else:
                cnt = 1
            max_count = max(max_count, cnt)


for i in range(N):
    for j in range(N):
        if i+1 < N: # 행 조건
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 바꾸고
                check(board)
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 복구
        if j+1 < N: # 열 조건
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 바꾸고
                check(board)
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 복구

print(max_count)

