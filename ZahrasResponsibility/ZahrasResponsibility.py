from datetime import datetime as dt

n , m = input().split()
n , m = int(n) , int(m)

b = 0
data = []

microS = dt.now()
microS = int(microS.strftime('%f'))

while b < n :

    microS2 = dt.now()
    microS2 = int(microS2.strftime('%f'))
    if microS2 - microS < 100000 :
        x = input().split()
        data.append(x)
    else :
        break

    microS = dt.now()
    microS = int(microS.strftime('%f'))

    b += 1

# print(f'n : {n} , m : {m} , data : {data} , i : {i}')

delta = []

for i in range(len(data)) :

    x1 = int(data[i][0])
    x2 = int(data[i][1])
    
    y = x1 - x2
    delta.append(y)

# print(delta)
happiness = []

if b > m :
    w = m
else :
    w = b

for i in range(w):

    x = max(delta)
    a = delta.index(x)

    happiness.append(data[a][0])
    data.pop(a)
    delta.pop(a)


for i in range(len(data)) :
    happiness.append(data[i][1])

sum = 0

for i in range(len(happiness)) :
    sum += int(happiness[i])

print(sum)