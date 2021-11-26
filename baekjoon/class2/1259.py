while True:
    num = int(input())
    if num == 0:
        break
    mylist = list(str(num))

    # print(mylist)
    # print(list(reversed(mylist)))

    if ''.join(mylist) == ''.join(list(reversed(mylist))):
        print('yes')
    else:
        print('no')