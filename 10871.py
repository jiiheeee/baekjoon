N, X = list(map(int, input().split()))

result = []
number_list = list(map(int, input().split()))
for data in range(N):
    if number_list[data]<X:
        result.append(number_list[data])

print(*result)


