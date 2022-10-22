temp = {"a", "b", "c"}
# set과 dict는 순서가 정해져 있지 않다.
# a
# c
# b

temp = enumerate(temp)
# tuple 형태로 데이터에 번호를 매겨준다.
# (0, 'c')
# (1, 'b')
# (2, 'a')

# for num, value in temp:
# print(num, value)
# enumerate는 값과 번호를 쪼갤 수 있다.
# 0 b
# 1 a
# 2 c

# a, b = (1, 2, 3)
# 변수 개수와 집어 넣을 데이터 개수가 같아야 한다.
# ValueError: too many values to unpack (expected 2)

a, b = {"name": "이름", "age": 12}.items()
# key : value 형태에 items를 이용하여 tuple 형태로 변환할 수 있다.
# ('name', '이름')
# ('age', 12)

print(a)
print(b)
