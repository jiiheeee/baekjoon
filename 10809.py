from string import ascii_lowercase #소문자는 lowercase, 대문자는 uppercase
alphbet_list = list(ascii_lowercase)

word = input()

result = []
for data in alphbet_list:
    result.append(word.find(data))
    # string.find() 괄호 안에 있는게 string에서 첫번째로 나오는 위치를 리턴

print(*result)