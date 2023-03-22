target_arr = [1, 1, 2, 2, 2, 8]
user_input = list(map(int, input().split()))

a = []
for idx in range(len(target_arr)):
    result = target_arr[idx]-user_input[idx]
    a.append(result)

for data in a:
    print(data, end=" ")