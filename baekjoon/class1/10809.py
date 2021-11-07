word = input()
small_letters = map(chr, range(ord('a'), ord('z')+1))
result = []
for c in small_letters:
    result.append(str(word.find(c)))
print(" ".join(result))