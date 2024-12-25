flag = 'yes'
x= input()
if len(x)== 4 or len(x) == 6 :
    for i in x :
        if i not in '1234567890' :
            flag = 'no'
            break
else :
    flag = 'no'
    
print(flag)