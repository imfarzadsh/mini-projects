# در مسایله ی برج هانوی باید دیسک هارا از A یه C به کمک B ببرییم
# به طوری که در هر حرکت تنها یک دیسک را بتوان جا به جا کرد
# دیسک شماره 2 بزرگتر از دیسک شماره 1 بوده
# و تنها دیسک کوچکتر میتواند روی دیسک بزرگتر قرار بگیرد

def hanoiTower(n , A , C , B) : # انتقال n دیسک از A به C توسط B
    if n == 1 :
        print(f'move disk {n} from {A} to {C}')
    else :
        hanoiTower(n-1 , A , B , C)
        print(f'move disk {n} from {A} to {C}')
        hanoiTower(n-1 , B , C , A)

hanoiTower(3 , 'Avali' , 'Akhari' , 'komaki')