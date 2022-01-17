# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    
    students = list(range(1, n + 1))
    #print(students)
    
    uniq_lost = list(set(lost) - set(reserve))
    uniq_reserve = list(set(reserve) - set(lost))
    lost = uniq_lost
    reserve = uniq_reserve
    
    #print(lost, reserve)
    
    students = list(set(students) - set(lost))
    
    #print(students)
    
    for r in reserve:
        before = r - 1
        after = r + 1
        
        if before in lost:
            lost.remove(before)
            students.append(before)
        elif after in lost:
            lost.remove(after)
            students.append(after)
        
    answer = len(students)
    
    return answer