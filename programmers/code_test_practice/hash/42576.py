# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    hash = {}
    
    for someone in participant:
        if(someone in hash):
            hash[someone] += 1
        else:
            hash[someone] = 1
            
    for someone in completion:
        if(someone in hash):
            hash[someone] -= 1
            
    for key, value in hash.items():
        if(value > 0):
            return key
    
    return ''