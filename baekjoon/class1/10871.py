a, b = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
print(" ".join([str(x) for x in nums if x < b]))