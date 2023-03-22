my_dict = {
    "ABC": 3,
    "DEF": 4,
    "GHI": 5,
    "JKL": 6,
    "MNO": 7,
    "PQRS": 8,
    "TUV": 9,
    "WXYZ": 10
}                   #dict 자료형 복습

user_input = input()
result = 0
for key, value in my_dict.items(): #items()는 각 row의 key, value를 각각 가져온다
    for char in user_input:
        if char in key: # in은 ~안에 있다면
            result += value

print(result)