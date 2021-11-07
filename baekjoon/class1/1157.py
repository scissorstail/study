word = input()
dic = {}

for char in word:
    upperChar = char.upper()
    
    if(upperChar in dic):
        dic[upperChar] += 1
    else:
        dic[upperChar] = 1

m = max(dic.values())
max_list = [k for k, v in dic.items() if v == m]

print(max_list[0] if max_list.__len__() == 1 else '?')