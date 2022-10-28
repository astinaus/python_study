# 클래스 상속
from animal import Animal
from cat import Cat
from dog import Dog

Animal.hello()

print()

a = Animal(12)
b = Cat("나옹", 5)
c = Dog("뽀삐", 3)

a.eat()
b.eat()
c.eat()
c.howl()

print()

a.get_age()
b.get_age()
# Cat 클래스에서 get_age 메소드를 선언하지 않았으나
# 부모 클래스인 Animal에 선언되어있기 때문에사용할 수 있다.
c.get_age()

print()

Animal.get_count()
Cat.get_count()
Dog.get_count()
