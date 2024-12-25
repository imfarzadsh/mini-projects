x = input()

if '+' in x :
    num= x.split('+')
    print(int(num[0])+int(num[1]))
elif '-' in x :
    num= x.split('-')
    print(int(num[0])-int(num[1]))
elif '*' in x :
    num= x.split('*')
    print(int(num[0])*int(num[1]))
elif '/' in x :
    num= x.split('/')
    if '/0' in x:
        print('-1')
    else: 
        print(int(num[0])/int(num[1]))
   