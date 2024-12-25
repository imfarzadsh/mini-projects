word = input()
word = word[::-1]
list_return = []
for char in word :
    if char.islower() :
        list_return.append(char.upper())
    elif char.isupper() :
        list_return.append(char.lower())
    else :
        list_return.append(char)

print(''.join(list_return))