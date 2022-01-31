# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    
    left = min(times)
    right = min(times) * n
    
    count = 0
    while(True):
        mid = (left + right) // 2
        
        mid_value = sum([mid // exam for exam in times])
        left_value = sum([left // exam for exam in times])
        right_value = sum([right // exam for exam in times])
         
        # print(left, mid, right)
        # print(left_value, mid_value, right_value)
        # print()
        
        if(left_value == mid_value == right_value):
            answer = mid 
            break
            
        if(mid_value < n):
            left = mid + 1
        elif(mid_value > n):
            right = mid
        else:
            if(left_value <= n):
                right = mid
            elif(right_value >= n):
                left = mid + 1
            else:
                answer = mid
                break
            
        # if(count > 10):
        #     break
        # count += 1
    return answer