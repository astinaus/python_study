# 문자열

name = 'astin'
age = 10

print(" 내 이름은 " + name + " 내 나이는 " + str(age))
print(f"내 이름은 {name} 내 나이는 {age}")
print("내 이름은 %s 내 나이는 %d"% (name, age))
print(f"{name=} {age=}")
print("내 이름은 {0} 내 나이는 {1}".format(name, age))
print("내 이름은 {n} 내 나이는 {a}".format(n=name, a=age))

# 튜플
my_tuple = (1,  2,3   ,4)

print(my_tuple)

for item in my_tuple:
    print(item)



# 딕셔너리
my_dict = {"name" : "astin", "age" : 12}

for key, value in my_dict.items():
    print(f"{key} 은/는 {value}")
  

# 조건문
data = 1

if data == 1:
    print("1이다")
elif data == 2:
    print("2다")
else:
    print("모르겠다")

data = int(input())

if data == 1:
    print("1이다")
elif data == 2:
    print("2다")
else:
    print("모르겠다")
    
# 반복문

def check_data():
    data = int(input())

    if data == 1:
        print("1이다")
    elif data == 2:
        print("2다")
    elif data == 3:
        print("3이다")
    elif data == 4:
        print("4다")
    else:
        print("모르겠다")

check_data()
check_data()
check_data()
x = 1

while True:
    print("가나다")
    if x >= 10:
        break
    else:
        x = x + 1
        
for item in [1,2,3,4]:
    print(item)


# 문자열 나누기
string = "가나다라 마바사"

char_list = string.split(' ')
print(char_list)

# 문자열 변경
change_string = string.replace('가' , '하')

print(id(string))
print(id(change_string))
print(change_string)

# 리스트

my_list = [1,2,3,4]

my_list[0] = 9

print(my_list)

for element in my_list:
    print(element)