x, y, w, h = map(int, input().split(' '))

# print(x, y, w, h)

# 왼쪽 경계선과의 거리
left = x

# 오른쪽 경계선과의 거리
right = w - x

# 위쪽 경계선과의 거리
top = h - y

# 아래쪽 경계선과의 거리
bottom = y

print(min([left, right, top, bottom]))