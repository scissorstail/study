while(True):
    try:
        value = input()
        if(not value):
            break
        a, b = map(int, value.split(' '))
        print(a + b)
    except:
        break