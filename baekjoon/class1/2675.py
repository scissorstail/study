count = int(input())
for i in range(count):
    a, b = input().split(' ')
    result = ''
    for c in b:
        result += (c * int(a))
    print(result)