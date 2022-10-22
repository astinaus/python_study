
temp = "가나다"
# 문자열은 요소를 번호로 가져올 수 있다.
# temp[0]='가'

# temp[0] = "라"
# 문자열은 불변이라 요소를 변경 할 수 없다.
# TypeError: 'str' object does not support item assignment

temp = "라"
# 변수에 다른 문자열을 넣을 수는 있다.
# temp='라'

del temp
# 변수를 삭제한다.
# 출력시 에러 발생
# NameError: name 'temp' is not defined

temp = "가나다"
temp = "라"
temp = "가나다"
# 같은 문자열, 숫자는 메모리 어딘가에 저장되어 다시 불러와진다.
# id(temp)=1242642310096
# id(temp)=1242642524048
# id(temp)=1242642310096

temp = "가나다\n라마바"
# 문자열을 여러줄로 출력하고 싶으면 \n 사용한다.
# 가나다
# 라마바

temp = """\
가나다
마바사
"""

# 가나다
# 마바사

temp = '그가 말했다. "안녕하세요"'
# 쌍따옴표를 문자열 안에 넣고 싶을 때 홑따옴표로 감싼다.
# 그가 말했다. "안녕하세요"

temp = "나는 생각했다. '잠온다'"
# 홑따옴표를 문자열 안에 넣고 싶을 때 쌍따옴표로 감싼다.
# 나는 생각했다. '잠온다'

temp = """그가 말했다. "안녕하세요" 나는 생각했다. '잠온다'\""""
# 쌍따옴표 홑따옴표 모두 넣을 경우 """ 또는 '''를 사용
# 그가 말했다. "안녕하세요" 나는 생각했다. '잠온다'"

temp = temp[0:3]
# 시퀀스는 대괄호를 이횽해서 잘라낼 수 있다.
# temp='그가 '

temp = "가나다라"
temp = temp[-1]
# temp='라'

# temp = temp[4]
# 범위를 넘는 요소 번호를 호출하면 에러가 발생한다.
# IndexError: string index out of range

temp = "가나다라"
temp = temp[-4]
# temp='가'

# temp = "가나다라"
# temp = temp[-5]
# IndexError: string index out of range

temp = "가나다라"
temp = temp[1:]
# 1번부터 끝까지
# temp='나다라'

temp = "가나다라"
temp = temp[:2]
# temp='가나'

temp = "가나다라"
temp = temp[1:100]
# 파이썬 문자열 컷팅은 유연하다.
# temp='나다라'

temp = "가나다라"
temp = temp[5:100]
# temp=''

temp = "가나다라"
temp = temp[-100:100]
# temp='가나다라'

# for item in temp:
# print(item)
# 문자열은 반복 가능하다.
# 가
# 나
# 다
# 라

temp = "가나" "다라"
# temp='가나다라'

temp = ("가나"
        "다라"
        "여러줄"
        "쓰고싶어요")
# temp='가나다라여러줄쓰고싶어요

# temp = len(temp)
# 문자열의 길이를 알고 싶으면 len 함수를 사용한다.
# temp=12

# temp = temp[len(temp)]
# IndexError: string index out of range

temp = temp[len(temp) - 1]
# temp='요'

temp = "가나다라"
temp = f"한글은 {temp}"
# f"" f''를 이용해서 변수를 문자열에 입력할 수 있다.
# temp='한글은 가나다라'

temp = "가나다라"
temp = "한글은 " + temp
# temp='한글은 가나다라'

temp = "가나다라"
temp = "한글은 %s" % temp
# temp='한글은 가나다라'

temp = "가나다라"
temp = "한글은 {arg1}".format(arg1=temp)
# temp='한글은 가나다라'

temp = "가나다라"
temp = temp.startswith("가나")
# 문자열의 시작을 확인하여 True False로 리턴한다.
# temp=True

temp = "가나다라"
temp = temp.endswith("다라")
# 문자열의 끝을 확인하여 True False로 리턴한다.
# temp=True

temp = "가나다라"
temp = temp.index("가")
# index는 해당 문자(문자열)의 요소 번호를 리턴한다.
# temp=0

temp = "1"
temp = temp.zfill(2)
# 빈 자리수를 0으로 채운다.
# temp='01'


temp = "1"
temp = temp.rjust(5, "!")
# 내가 원하는 문자로 채울 수 있다.
# temp='!!!!1'

print(f"{temp=}")

