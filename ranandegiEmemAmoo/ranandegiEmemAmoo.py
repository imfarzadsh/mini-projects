N , L = input().split()

N = int(N)
L = int(L)

data = []
for i in range(N) :
    data.append(input().split())
    
# print(data)

time = 0
repeat = [0]
for i in range(len(data)) :

        distance = int(data[i][0])
        greenTime = int(data[i][1])
        redTime = int(data[i][2])
        
        time += distance
        time -= repeat[0]
        repeat[0] = distance

        remaining = time % (greenTime + redTime) 

        if remaining < greenTime :
              continue
        else :
              time += abs(greenTime + redTime - remaining)

time += (int(L) - repeat[0])

print(time)