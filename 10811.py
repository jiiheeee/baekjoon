def reverse_data(data, baguni: list):
    # """
    #     data의 0번째부터 1번째까지 baguni를 뒤집는다.
    #     ex)  baguni = [1, 2, 3, 4, 5]
    #         reverse =     [2, 4]
    #               x =    [4, 3, 2]
    # """
    a, b = data[0]-1, data[1]-1
    x = baguni[a:b+1]  # 복사
    x.reverse()

    for idx, value in enumerate(range(a, b+1)):
        baguni[value] = x[idx]

    # pass를 안쓰고 진행하면 다음 문법에서 에러가 날 수 있으니 일단 쓰고 함수가 잘 작동하면 지우기 
    # 디버깅할때 에러로 걸리는거 방지
baguni_cnt, T = list(map(int, input().split()))

baguni = []
reverse = []

for data in range(1, baguni_cnt+1):
    baguni.append(data)

for i in range(T):
    reverse.append(list(map(int, input().split())))

for idx in reverse:
    reverse_data(idx, baguni)
        # 복잡하면 함수로빼서 따로 적기

print(*baguni)