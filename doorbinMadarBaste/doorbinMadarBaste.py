x1 , y1 = map(int , input().split())
x2 , y2 = map(int , input().split())
x3 , y3 = map(int , input().split())

if x1 == x2 :
    if y3 == y1 :
        y4 = y2 + y3 - y1
        x4 = x2 + x3 - x1
    elif y3 == y2 :
        y4 = y1 + y3 - y2
        x4 = x1 + x3 - x2
elif x1 == x3 :
    if y2 == y1 :
        y4 = y2 + y3 - y1
        x4 = x2 + x3 - x1
    elif y2 == y3 :
        y4 = y1 + y2 - y3
        x4 = x1 + x2 - x3
elif x2 == x3 :
    if y1 == y2 :
        y4 = y1 + y3 - y2
        x4 = x1 + x3 - x2
    elif y1 == y3 :
        y4 = y1 + y2 - y3
        x4 = x1 + x2 - x3

# print(x4 , y4)


# method : 2

# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())

# if x1 == x2:
#     x4 = x3
# elif x1 == x3:
#     x4 = x2
# else:
#     x4 = x1

# if y1 == y2:
#     y4 = y3
# elif y1 == y3:
#     y4 = y2
# else:
#     y4 = y1

# print(x4, y4)
