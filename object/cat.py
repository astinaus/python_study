from animal import Animal

# Animal 클래스를 상속받아 새로 Cat 클래스 선언
class Cat(Animal):

    count = 0

    def __init__(self,
                 name: str = "냥",
                 age: int = 0
                 ):
        """""

        Args:
            name (str, optional): 고양이의 이름. 기본값은 "냥".
            age (int, optional): 고양이의 나이. 기본값은 0.
        """""
        # super 은 부모 클래스의 메소드를 사용할 때 선언한다.
        super().__init__(age)

        self.name = name

        Cat.count = Cat.count + 1

        return

    def eat(self):
        print(f"고양이 '{self.name}'이 음식을 먹었습니다.")

    @classmethod
    def get_count(cls):
        print(f"고양이가 {cls.count}마리 생성되었습니다.")