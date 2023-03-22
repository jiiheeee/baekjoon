def solution(array, height):
    cnt = 0
    for data in array:
        if data > height:
            cnt += 1
    return cnt

print(solution([149, 180, 192, 170], 167))