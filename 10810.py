N, M = list(map(int, input().split()))

Baguni = []
for cnt in range(N):
    Baguni.append(0)

for data in range(M):
    _from, _to, target_ball = list(map(int, input().split()))
    _from = _from -1
    for idx in range(_from, _to):
        Baguni[idx] = target_ball

print(*Baguni)

