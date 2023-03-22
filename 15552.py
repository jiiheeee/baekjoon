import sys
number = int(sys.stdin.readline())

number_list = []
for data in range(number):
    A, B = list(map(int, sys.stdin.readline().split()))
    result = A + B
    number_list.append(str(result))

for idx in number_list:
    sys.stdout.writelines(idx)
    sys.stdout.writelines("\n")