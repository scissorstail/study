a, b = map(int, input().split(' '))

a_list = list(map(int, str(a)))
b_list = list(map(int, str(b)))

a_list.reverse()
b_list.reverse()

a_list = list(map(str, a_list))
b_list = list(map(str, b_list))

a = int(''.join(a_list))
b = int(''.join(b_list))

print(max(a, b))