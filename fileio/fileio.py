# 파일 생성 및 데이터 입력

# keyword argument는 생략가능(생략하면 순서를 지켜야함)
# mode ='w' 는 파일 생성 (write)
# UTF-8 = Unicode Transpormation Format - 8bit
file_editor = open(file="fileio/test.txt", mode="w", encoding="utf-8")

file_editor.write("안녕하세요.")

# 파일을 open 했다면 반드시 close 해주는 것이 좋다.
file_editor.close()

