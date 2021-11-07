T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):
    count = 0
    sum = 0
    for res in list(map(str, input())):
        if(res == "O"):
            count += 1
            sum += count
        else:
            count = 0
    print(sum)