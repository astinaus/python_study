# Animal 클래스 선언
class Animal:
    # 클래스 변수 선언
    count = 0
    # 초기화 함수 정의
    def __init__(self,
                 age: int = 0
                 ):
        """

        Args:
            age (int, optional): 동물의 나이. 기본값은 0.
        """
        # 인스턴스 필드
        self.age = age

        self.name = f"{Animal.count}번"

        Animal.count = Animal.count + 1

        return
    # 인스턴스 메소드
    def eat(self):
        print(f"동물 {self.name}이 음식을 먹었습니다.")

    def get_age(self):
        print(f"동물 '{self.name}'의 나이는 {self.age}살 입니다.")

    # @ = Annotation
    # 클래스 메소드
    @classmethod
    def get_count(cls):
        print(f"동물이 {cls.count}마리 생성되었습니다.")

    # 정적 메소드
    @staticmethod
    def hello():
        print(f"동물 농장에 오신 것을 환영합니다.")
