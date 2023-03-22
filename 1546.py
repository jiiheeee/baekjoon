T = int(input())
score = list(map(int, input().split()))

sum = 0
for data in score:
    sum = sum + data

print(sum/T/max(score)*100)