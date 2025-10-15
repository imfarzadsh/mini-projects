import random as rd

smallAlphabet = [chr(x) for x in range(ord('a') , ord('z') +1 )]
# print(s , t , n , smallAlphabet)

def sYES_tNO(s , t , n) :

    result = s
    A = n - len(s)

    if n < len(s) :
        return '-1'
    if t in s :
        return '-1'

    x = rd.choices(smallAlphabet , k = A )
    y = ''.join(x)

    if t in y :
        sYES_tNO(s , t ,n)
    else :
        result += y
        return result

s = input().strip()
t = input().strip()
n = int(input().strip())

result = sYES_tNO(s , t ,n)
print(result)