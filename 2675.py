number = int(input())

for data in range(number):
    N, word = list(map(str, input().split()))  
    for i in word:
        print(i*int(N), end="") 
        # end=""는 공백없이 출력
    print()
    # print()는 엔터 출력

