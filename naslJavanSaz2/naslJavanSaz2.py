playersInfo = eval(input())

playersAge = []
for i in range(len(playersInfo)) :
    playersAge.append(playersInfo[i]['age'])

playersAge.sort()

endList = []
for i in playersAge :
    for a in range(len(playersInfo)) :
        if i == playersInfo[a]['age'] :
            endList.append(playersInfo[a])

endTuple = tuple(endList)

print(endTuple)