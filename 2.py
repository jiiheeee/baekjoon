number_list = []
def solution(n):
    for data in range (1,n+1):
        a = n%data
        number_list.append(a)
    for idx, data in enumerate(number_list):
        if data == 1:
            return idx+1