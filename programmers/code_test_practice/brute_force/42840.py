# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
        
    user1 = [1,2,3,4,5]
    user2 = [2,1,2,3,2,4,2,5]
    user3 = [3,3,1,1,2,2,4,4,5,5]
    
    user1_count = 0
    user2_count = 0
    user3_count = 0
    for num in range(len(answers)):
        if user1[num % 5] == answers[num]:
            user1_count += 1
        if user2[num % 8] == answers[num]:
            user2_count += 1
        if user3[num % 10] == answers[num]:
            user3_count += 1
                
    
    if user1_count == max(user1_count, user2_count, user3_count):
        answer.append(1)
    if user2_count == max(user1_count, user2_count, user3_count):
        answer.append(2)
    if user3_count == max(user1_count, user2_count, user3_count):
        answer.append(3)
    return answer