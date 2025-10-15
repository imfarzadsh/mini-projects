

def factorial(n) :
    result = 1
    for i in range(1 , n+1) :
        result *= i
    return result

def tarkib(b , a) :
    return int(factorial(a) / (factorial(b)*factorial(a-b)))


def khayyamPascal(n) :

    myList = []

    for i in range(n+1) :
        result = []
        for j in range(i+1) :
            result.append(tarkib(j , i))
        myList.append(result)

    for result in myList :
        print(' '.join(map(str ,result )).center(n+100 ))



n = int(input('enter n : '))
khayyamPascal(n)

