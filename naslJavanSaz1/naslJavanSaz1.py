playersInfo = eval(input())

all25 = []
for i in range( 0 , len(playersInfo) ) :
    if int(playersInfo[i]['age']) < 25 :
        all25.append(playersInfo[i]['club'])

# print(all25)

nameList = []
countList = []
for i in range( 0 , len(playersInfo) ) :
    nameList.append(playersInfo[i]['club'] )
    countList.append(all25.count(playersInfo[i]['club'])) 

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
for i in range(0 , len(playersInfo)) :
    all.append(playersInfo[i]['club'])

print(all)
print(fine)
