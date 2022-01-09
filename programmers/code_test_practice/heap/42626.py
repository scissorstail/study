# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    h = scoville
    heapq.heapify(h)
    
    count = 0
    answer = 0
    first = heapq.heappop(h)
    while(True):        
        if(first >= K):
            answer = count
            break
        
        if not h:    
            answer = -1
            break
        
        second = heapq.heappop(h)
        
        first = heapq.heappushpop(h, first + (second * 2)) # 값을 힙에 추가하면서 가장 작은 값도 반환 
                
        count += 1

    return answer