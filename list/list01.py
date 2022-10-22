temp = [1, 2] + [3, 4]
# 리스트를 더하면 리스트가 합쳐진다.
# [1, 2, 3, 4]

temp.append(5)
# 리스트 안에 값을 추가한다.
# [1, 2, 3, 4, 5]

temp.remove(1)
# 리스트에 있는 값을 삭제한다.
# [2, 3, 4, 5]

temp = [1, 1, 1, 1]
temp.remove(1)
# 같은 데이터를 모두 지우지 않고 하나만 지운다.
# [1, 1, 1]

temp = [1, 1, 1, 1]


def check(num):
    if num == 1:
        return False
    else:
        return True


# print(check(1213))
# print(True)

temp = [1, 2, 3, 1, 1]
temp = filter(check, temp)
temp = list(temp)
# [2, 3]

# temp = list(filter(check, [1,1,1,1]))

# print(temp)

temp = [1, 2, 3, 4, 5]
temp = [
    [1, 2],
    [3, 4]
]

# print(temp[0])
# print(temp[0][0])

temp = [
    (1, 2),
    (3, 4)
]

temp = [
    {"a", "c"},
    {"b", "d"}
]

temp = [
    {"key" : "value", "name" : "이름"},
    {"b" : "d", "aa" : "dd"}
]

# print(temp[0])
# {'key': 'value', 'name': '이름'}


# print(temp[0]["name"])
# 이름

