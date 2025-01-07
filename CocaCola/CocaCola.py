AmountDue = 50

while AmountDue > 0 :
    for i in [int(input())] :
        if i == 25 or i == 10 or i == 5 :
            AmountDue = AmountDue - i
            if AmountDue > 0 :
                print(f'Amount Due: {AmountDue}')
            else :
                print(f'Change Owed: {abs(AmountDue)}')
                break
        else :
            print(f'Amount Due: {AmountDue}')
            continue