SL = []
for aa in range(1, 31):
    SL.append(aa)

for data in range(1, 29):
    S = int(input())
    SL.remove(S)

print(min(SL), max(SL))