age = int(input()) # دریافت سن کاربر

# پیشنهاد فیلم بر اساس سن
if age < 12 :
    print('You can watch animations suitable for children.')
elif 12 <=age < 18 :
    print('You can watch series and movies suitable for teenagers.')
else :
    print('You can watch series and movies suitable for adults.')