# 파일 읽기

# mode = "r" 은 파일 읽기 (read)
file_editor = open(file="fileio/test.txt", mode="r", encoding="utf-8")

# read()는 파일에 있는 모든 데이터를 가져온다.
my_text = file_editor.read()

file_editor.close()

print(my_text)

