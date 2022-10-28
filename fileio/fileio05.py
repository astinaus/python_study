# 파일 삭제

import os

# 1번 방법
# if os.path.exists("fileio/test.txt"):
#     os.remove("fileio/test.txt")

# 2번 방법
# os.system("rm fileio/test.txt")
# 폴더를 지우고 싶다면 -r 을 붙여주면 된다.
# -rf는 경고나 에러를 무시하고 강제적으로 삭제한다.
# os.system("rm -r fileio")

