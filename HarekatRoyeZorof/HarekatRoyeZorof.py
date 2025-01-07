a , b , c = map(float , input().split())

if a == b == c :
    print(0)
elif ( a + b == 2*c ) or ( a + c == 2*b ) or ( b + c == 2*a ) :
    print(1)
else :
    print(2)