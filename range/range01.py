temp = range(10)
# range(0, 10)

temp = list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

temp = list(range(5, 10))
# [5, 6, 7, 8, 9]

temp = list(range(3, 30, 3))
# [3, 6, 9, 12, 15, 18, 21, 24, 27]

# print(temp)

temp = list(range(0, 10))

# for item in temp:
#     print("안녕")

# temp = [item for item in range(0, 10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 대괄호를 씌우면 list로 만들어진다.

# temp = (item for item in range(0, 10))
# <generator object <genexpr> at 0x000002A810B943C0> 소괄호를 씌우면 generator가 만들어진다.

# temp = {item for item in range(0, 10)}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 중괄호를 씌우면 set이 만들어진다.

temp = {"안녕" for item in range(0, 10)}
# set은 중복된 값을 지우기 때문에 하나만 입력된다.
# {'안녕'}

temp = ["안녕" for item in range(0, 10)]
# list로 만들면 중복된 값도 모두 range 안의 범위 만큼 입력된다.
# ['안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕']

print(temp)
