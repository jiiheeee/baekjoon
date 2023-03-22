number = []
for data in range(9):
    X = int(input())
    number.append(X)

print(max(number))
print(number.index(max(number))+1)