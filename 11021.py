T = int(input())

add_list = []
chart = []
case_list = []

for data in range(T):
    A, B = list(map(int, input().split()))
    result = A + B
    add_list.append(result)

for idx in range(1, T+1):
    data_1 = '"Case", "#"f"{idx}:"'
    chart.append(data_1)

for aa in range(T):
    print(f"Case #{aa+1}: {add_list[aa]}")

#result = [6, 4, 7]
#for aa in range(3):
#    print(f"Case #{aa+1}: {result[aa]}")
"""
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7
"""