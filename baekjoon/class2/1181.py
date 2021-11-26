T = int(input())

mylist = []
for _ in range(T):
    mylist.append(input())

my_obj = {}
for word in list(set(mylist)):
    len_str = str(len(word))
    if len_str in my_obj:
        my_obj[len_str].append(word)
    else:
        my_obj[len_str] = [word]

my_lists = []        
for a in my_obj:
    word_list = my_obj[a]
    my_lists.append([int(a), sorted(word_list)])

my_sorted_lists = sorted(my_lists, key=lambda x: x[0])

result_list = []
for x in my_sorted_lists:
    result_list.extend(x[1])

for word in result_list:
    print(word)