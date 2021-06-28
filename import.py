#猜數字遊戲

import random

##################################################################

r = random.randint(1, 100)
count = 0   #猜測次數計算，寫在while迴圈外以免歸零

while True:
    count = count + 1   #count = count + 1也可寫成count += 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('猜對喔~')
        print('這是你猜的第', count, '次') #這裡再寫一次讓猜對時也會顯示
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('這是你猜的第', count, '次')  #直接寫在底下只需寫一次




