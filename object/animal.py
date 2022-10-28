
class Animal:
    def __init__(self, age) -> None:
        self.age = age
    
    def eat(self):
        print(f"동물이 음식을 먹었습니다.")
        
    def get_age(self):
        print(f"동물의 나이는 {self.age}살 입니다.")
    