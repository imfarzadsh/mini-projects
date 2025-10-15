n , k = input().split()
n , k = int(n) , int(k)
# print(n , k)

homes = []

for i in range(1 , n+1 ) :

    if i % 2 != 0 :
        homes.append(i)


for j in range(n , 0 , -1) :
    if len(homes) < k :
        if j % 2 == 0 :
            homes.append(j)


number = 0
for i in homes :
    if i+1 in homes :
        number += 1

print(number)
