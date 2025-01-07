temperature = int(input())

if temperature > 6000 or temperature <= 273 :
    exit()
elif temperature > 100 :
    print('Steam')
elif temperature < 0 :
    print('Ice')
else :
    print('Water')