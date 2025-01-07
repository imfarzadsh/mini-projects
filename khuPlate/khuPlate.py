import string

def main() :
    plate =  input()
    x = is_valid(plate)
    print(x)


def alphabet(v) :
    temp1 = ''
    for i in v :
        if i in string.ascii_uppercase or i in string.ascii_lowercase :
            temp1 += i
        else :
            continue
    return temp1       


def get_numbers(v) :

    temp2 = ''

    for i in v :
        if i.isdigit() == True :
            temp2 += i
        else :
            continue
    return temp2

def get_others(v) :

    temp3 = ''

    for i in v :
        if i in string.ascii_uppercase or i in string.ascii_lowercase :
            continue
        elif i.isdigit() == True :
            continue
        else :
            temp3 += i
    return temp3




def is_valid(plate) :

    z1 = alphabet(plate)
    z2 = get_numbers(plate)
    z3 = get_others(plate)

  
    if len(plate) < 2 or len(plate) > 6 :
        return 'Invalid'
    elif len(z1) < 2 :
        return 'Invalid'
    elif z1 not in plate :
        return 'Invalid'
    elif z2 and z2[0] == '0' :
            return 'Invalid'
    elif z3 != '' :
        return 'Invalid'
    else :
        return 'Valid'

main()