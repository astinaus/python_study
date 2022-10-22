def solution(array : list, height : int):
    
    answer = 0
    for i in array:
        if i > height:
            answer += 1
        else:
            continue
    
    return answer