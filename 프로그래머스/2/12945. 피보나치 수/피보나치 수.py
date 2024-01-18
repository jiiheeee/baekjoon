def solution(n):
    F = []
    for data in range(n+1):
        if data == 0 or data == 1:
            data = data + 0
            F.append(data)
        else:
            data = F[data-2] + F[data-1]
            F.append(data)
    result = F[n]%1234567
    return(result)