x = input()
x = x.replace(' ' , '')

if 'hello' in x.lower() :
    print('0$')
elif 'h' in x[0].lower() :
    print('20$')
else :
    print('100$')