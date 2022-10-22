# import math as m
# 인용할 라이브러리의 별명을 지어준다.

# from math import pow
# 라이브러리에서 특정 함수만 꺼내온다.

temp = None

temp = True and False

# assert temp

# print(temp)

# for item in range(10):
#     # 처음
#     if item == 5:
#         # 반복문의 처음으로 돌아감
#         continue
#     elif item == 8:
#         # 반복문을 멈춤
#         break
#     else:
#         print(item)

# 0
# 1
# 2
# 3
# 4
# 6
# 7

# try:
#     temp = "가나다"
#     temp[0] = "아"
# except Exception as e:
#     print(e)
#     # e.with_traceback()
#     # print("에러가 발생했습니다.")
# finally:
#     print("마지막으로 할 것은 하겠습니다.")

# print("넘어왔습니다.")

# temp = 1

# for i in range(10):
#     pass

# print(temp)

# temp = 1

# def my_func():
#     global temp
#     temp = 3
#     return temp

# print(my_func())
# print(temp)

# raise Exception("내가 만든 에러")

# parameter, 파라미터
# def my_func(num):
#     print(num)

# my_func(12)
# argument, 아규먼트, 인자, 인수

# my_func = lambda num : print(num)
# def my_func(num): return print(num)

# my_func(12)

# temp = list(filter(lambda num : num != 1,[1, 2, 3, 1]))
# [2, 3]

# print(temp)

# def my_func():
#     while True:
#         yield 1
#         yield 2
#         yield 3


# my_yield_data = my_func()

# for item in my_yield_data:
#     print(item)

# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))

def check_str(data : str):
    return data.endswith("마")
# False


print(check_str("가나다"))
