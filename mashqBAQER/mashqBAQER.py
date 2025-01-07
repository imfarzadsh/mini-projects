x = input()
x = x.split(' ')

x0 = int(x[0])
x1 = int(x[1])
x2 = int(x[2])

sumX = x0 + x1 + x2
if x0 == 0 or x1 == 0 or x2 == 0 :
    print('No')
elif x0 == 180 or x1 == 180 or x2 == 180 :
    print('No')
elif sumX == 180 :
    print('Yes')
else :
    print('No')


# method : 2

# a, b, c = map(int, input().split())

# if a + b + c == 180 and a > 0 and b > 0 and c > 0:
#     print("Yes")
# else:
#     print("No")

# method : 3

# def is_triangle(angle1, angle2, angle3):
#     # بررسی مجموع زوایا و عدم وجود زاویه صفر یا منفی
#     if angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180:
#         return "Yes"
#     else:
#         return "No"

# # دریافت ورودی از کاربر
# angles = input().split()
# angle1 = int(angles[0])
# angle2 = int(angles[1])
# angle3 = int(angles[2])

# # نمایش نتیجه
# print(is_triangle(angle1, angle2, angle3))
