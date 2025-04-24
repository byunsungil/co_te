# 27160

N = int(input())

STRAWBERRY = [] 
BANANA = []
LIME = [] 
PLUM = []

for _ in range(N):
    card, num = input().split()
    num = int(num)
    if card == "STRAWBERRY":
        STRAWBERRY.append(num)
    elif card == "BANANA":
        BANANA.append(num)
    elif card == "LIME":
        LIME.append(num)
    else:
        PLUM.append(num)

if (sum(STRAWBERRY)== 5 or sum(BANANA)== 5 or sum(PLUM)== 5 or sum(LIME) == 5):
    print("YES")
else:
    print("NO")