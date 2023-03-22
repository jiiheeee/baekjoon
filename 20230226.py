class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}이(가) 밥을 먹습니다.")
    def sleep(self):
        print(f"{self.name}이(가) 잠을 잡니다.")


a = Person("박지성", 31)
b = Person("박요선", 58)
c = Person("박준호", 58)
d = Person("박지희", 28)

print(a)
print(b)
print(c)
print(d)