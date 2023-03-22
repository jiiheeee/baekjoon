# baguni_cnt, T = list(map(int, input().split()))

# exchange_baguni = []
# baguni = []

# for i in range(1, baguni_cnt+1):
#     baguni.append(i)

# for data in range(T):
#     exchange_baguni.append(list(map(int, input().split())))

# for exchange in exchange_baguni:
#     baguni[exchange[0]-1], baguni[exchange[1]-1] = baguni[exchange[1]-1], baguni[exchange[0]-1]

# print(*baguni)


baguni_cnt, T = list(map(int, input().split()))

baguni = []
exchange_baguni = []

for data in range(1, baguni_cnt+1):
    baguni.append(data)

for idx in range(T):
    exchange_baguni.append(list(map(int, input().split())))

for i in exchange_baguni:
    baguni[i[0]-1], baguni[i[1]-1] = baguni[i[1]-1], baguni[i[0]-1]

print(*baguni)