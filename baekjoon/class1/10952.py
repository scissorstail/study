while(True):
    try:
        value = input()
        a, b = map(int, value.split(' '))
        if(a == 0 and b == 0):
            break
        print(a + b)
    except:
        break