https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        while(len(progresses) > 0):
            task = progresses.pop(0)
            if(task < 100):
                progresses.insert(0, task)
                break
            else:
                speeds.pop(0)
                count += 1
                
        if(count > 0):
            answer.append(count)
    
    return answer