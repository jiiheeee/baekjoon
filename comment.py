# 나이와 주소를 받아서 연령대와 사는 곳을 출력하는 코드

age = int(input())

if 20<=age<=29:
    print("20대 입니다")
elif 30<=age<=39:
    print("30대 입니다")
elif 40<=age<=49:
    print("40대 입니다")
else:
    print("20대 30대 40대가 아닙니다.")

adress = input()

if adress == "서울":
    print("서울에 살고 있습니다.")
else:
    print("서울에 살고 있지 않습니다.")

