# 25305

N,k = map(int,input().split()) # 응시자수, 상받는사람수

score = list(map(int,input().split())) # 점수

cut = sorted(score,reverse=True)

print(cut[k-1])