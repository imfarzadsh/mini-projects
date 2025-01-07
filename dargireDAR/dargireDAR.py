dar , masoud = input().split() , input().split() # دریافت عرض و طول در و مسعود

darW , darH = int(dar[0]) , int(dar[1]) # مشخص کردن طول و عرض در
masoudW , masoudH = int(masoud[0]) , int(masoud[1]) # مشخص کردن طول و عرض مسعود

if (darW >= masoudW and darH >= masoudH) :
    print('yes')
else :
    print('no')

# with map :

# x1, x2 = map(int, input().split())
# y1, y2 = map(int, input().split())

# if x1 >= y1 and x2 >= y2:
#     print("yes")
# else:
#     print("no")
