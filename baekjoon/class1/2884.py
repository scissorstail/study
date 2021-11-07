h, m = map(int, input().split(' '))

if m - 45 < 0:
    h -= 1
    m = 60 + m - 45
else:
    m -= 45

if h < 0:
    h = 24 + h

print(h, m)