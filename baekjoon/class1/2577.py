a = int(input())
b = int(input())
c = int(input())

num = str(a * b * c)
table = {}

for c in num:
    if c in table: 
        table[c] += 1
    else:
        table[c] = 1

for c in map(str, range(10)):
    if c in table:
        print(table[c])
    else:
        print('0')