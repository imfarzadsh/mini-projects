x = input()

for i in x :
    if i == '+' : 
        num = x.split('+')
        num1 = int(num[0])
        num2 = int(num[1])
        result= num1+num2
        break
    elif i == '-' :
        num = x.split('-')
        num1 = int(num[0])
        num2 = int(num[1])
        result= num1-num2
        break
    elif i == '*' :
        num = x.split('*')
        num1 = int(num[0])
        num2 = int(num[1])
        result= num1*num2
        break
    elif i == '/' :
        if '/0' in x:
            print('-1')
        else: 
            num = x.split('/')
            num1 = int(num[0])
            num2 = int(num[1])
            result= num1/num2
        break
print(result)
            
