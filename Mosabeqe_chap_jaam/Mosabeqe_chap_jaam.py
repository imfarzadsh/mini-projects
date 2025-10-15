num = int(input())

output = ''
sum = 0

for i in range(1 ,num+1 ) :

    sum += i

    if i == num :
        output += f'{i} ='
    else :
        output += f'{i} + '


print(output , sum)