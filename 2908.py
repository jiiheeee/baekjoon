a, b = input().split()
a = list(map(str, a.strip())) #map은 int를 a.strip() 각 요소에 int를 씌운다
b = list(map(str, b.strip()))

a.reverse()
b.reverse()
number_1 = "".join(a)
number_2 = "".join(b) #()안에 문자열을 ""사이에 끼고 합친다
                      #ex) " ".join(["a", "b", "c"])
                      #                              a b c

if int(number_1) < int(number_2):
    print(number_2)
else:
    print(number_1)