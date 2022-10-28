# 파일 읽기

# mode = "r" 은 파일 읽기 (read)
file_editor = open(file="fileio/test.txt", mode="r", encoding="utf-8")

# readlines()는 파일 데이터를 한줄씩 배열로 가져온다.
my_text = file_editor.readlines()

file_editor.close()

print(my_text)
