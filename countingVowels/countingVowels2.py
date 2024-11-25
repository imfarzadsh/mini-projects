word = input()
word = word.lower()
x = 0
for char in word :
    if char in 'aeiou' :
        x += 1
print(x)
