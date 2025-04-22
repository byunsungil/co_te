# 1913

N = int(input()) 
num = int(input()) # 좌표를 찾는 수

result = [[0]*N for _ in range(N)]  # 0으로 채워진 리스트 생성

# 위 > 오 > 아래 > 왼
dx = [-1, 0, 1, 0] # x좌표 이동
dy = [0, 1, 0, -1] # y좌표 이동

x = N // 2
y = N // 2
result[x][y] = 1 # 시작 지점 지정 1

if num == 1:
    spot = (x+1, y+1)

dir = 0
step = 1 # 방향을 2번 바꾸면 1씩 증가
start = 2 # 2부터 시작

while start <= N*N:
    for _ in range(2): # 방향 2번 마다
        for _ in range(step):

            x += dx[dir]
            y += dy[dir]

            result[x][y] = start

            if start == num:
                spot = (x+1, y+1)
            
            if start > N*N:
                break
            start += 1
        dir = (dir + 1) % 4 # 위>오>아래>왼 방향
    step += 1

for row in result:
    print(" ".join(map(str, row)))

print(*spot) # 리스트, 튜플의 요소를 한 줄에 공백으로 출력하고 싶을 때


