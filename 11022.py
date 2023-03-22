T = int(input())

add_list = []
chart = []
case_list = []
number_list = []

for data in range(T):
    number = list(map(int, input().split()))
    A, B = number[0], number[1]
    dd = f"{A}+ {B}"
    result = A + B
    number_list.append(dd)
    add_list.append(result)

for idx in range(1, T+1):
    data_1 = '"Case", "#"f"{idx}:"'
    chart.append(data_1)

for aa in range(T):
    print(f"Case #{aa+1}: {number_list[aa]} = {add_list[aa]}")