TimeS = int(input()) # دریافت تایم بر اساس ثانیه 

hh  = TimeS // 3600
hh2 = TimeS % 3600

mm = hh2 // 60

ss = hh2 % 60

print(f'{hh:02d}:{mm:02d}:{ss:02d}') # تبدیل ثانیه به زمان