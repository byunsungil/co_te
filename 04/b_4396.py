# 4396

# 첫 번째 줄에는 10보다 작거나 같은 양의 정수 n이 입력된다. 다음 n개의 줄은 지뢰의 위치를 나타낸다. 각각의 줄은 n개의 문자를 사용하여 한 행을 나타낸다. 온점(.)은 지뢰가 없는 지점이며 별표(*)는 지뢰가 있는 지점이다. 다음 n개의 줄에는 길이가 n인 문자열이 입력된다. 이미 열린 칸은 영소문자 x로, 열리지 않은 칸은 온점(.)으로 표시된다. 예제 입력은 문제 설명에서의 가운데 그림과 상응한다.

# 출력은 각각의 위치가 정확하게 채워진 판을 표현해야 한다. 지뢰가 없으면서 열린 칸에는 0과 8 사이의 숫자가 있어야 한다. 지뢰가 있는 칸이 열렸다면 지뢰가 있는 모든 칸이 별표(*)로 표시되어야 한다. 다른 모든 지점은 온점(.)이어야 한다.

N = int(input())

loc_boom = [list(input().strip()) for _ in range(N)]
game = [list(input().strip()) for _ in range(N)]

result = [['.' for _ in range(N)] for _ in range(N)]
boom_clicked = False

for i in range(N):
    for j in range(N):
        if game[i][j] == 'x':
            if loc_boom[i][j] == '*':
                boom_clicked = True  # 지뢰 밟음
            else:
                cnt = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < N:
                            if loc_boom[ni][nj] == '*':
                                cnt += 1
                result[i][j] = str(cnt)

if boom_clicked:
    for i in range(N):
        for j in range(N):
            if loc_boom[i][j] == '*':
                result[i][j] = '*'

for line in result:
    print("".join(line))

 

