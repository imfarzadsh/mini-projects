x = int(input('please enter your number between 1 and 9 :'))
if 1 <= x <= 9 :
    print( f' number : {((x * 2 + 8 + x - 2)/3 - x)* 4 }')
    
else :
    print("*** input number is not between 1 and 9 ***")
    