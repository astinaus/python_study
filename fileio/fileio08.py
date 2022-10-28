import pickle

# 바이너리 파일 입력
with open(file="fileio/bin.pickle", mode="bw") as file_editor:
    pickle.dump([1,2,3], file_editor)
