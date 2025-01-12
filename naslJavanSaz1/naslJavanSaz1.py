x = input()

y = eval(x)


all25 = []
for i in range( 0 , len(y) ) :
    if int(y[i]['age']) < 25 :
        all25.append(y[i]['club'])

# print(all25)

nameList = []
countList = []
for i in range( 0 , len(y) ) :
    nameList.append(y[i]['club'] )
    countList.append(all25.count(y[i]['club'])) 

# print(countList)
# print(nameList)

endList = []
for i in range(0 , len(countList)) :
    if countList[i] == max(countList) :
        if nameList[i] not in endList :
            endList.append(nameList[i])

# print(endList)

fine = 'Mr.Ghalenoei says : Thank you'
if max(countList) == 0 :
    fine = 'Mr.Ghalenoei says : Our clubs should be producing more high quality young players.'
else :
    for i in range(len(endList)) :
        if i == len(endList) - 1 :
            fine += f' {endList[i]}'
        elif i == len(endList) - 2 :
            fine += f' {endList[i]} and'
        else :
            fine += f' {endList[i]},'
    fine += ' for producing high quality young players.'

all = []
for i in range(0 , len(y)) :
    all.append(y[i]['club'])

print(all)
print(fine)
