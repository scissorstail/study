# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    path = []
    
    results = []
    
    find(numbers, target, path, results)
    # print(results)
    answer = len(results)
    
    return answer


def find(numbers, target, path, results):
    # print(numbers, path)
    if len(numbers) == 0:
        if(sum(path) == target):
            results.append(sum(path))
        return
    
    current = numbers.pop()
    
    path.append(current * -1)
    find(numbers, target, path, results)
    path.pop()
    
    path.append(current * +1)
    find(numbers, target, path, results)
    path.pop()

    numbers.append(current)
    
    return