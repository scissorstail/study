T = int(input())
count = 1
found = 0
while True:
    if '666' in str(count):
        found = found + 1
    
    if found == T:
        print(count)
        break
    
    count += 1