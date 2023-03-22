now_time = list(map(int, input().split()))
time = int(input())

H, M = now_time[0], now_time[1]
result_M = time + M

add_H = result_M//60
result_M = result_M%60

result_H = H + add_H
if result_H>=24:
    result_H = result_H - 24

print(result_H, result_M)