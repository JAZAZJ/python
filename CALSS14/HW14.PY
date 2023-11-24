# import random

# num1 = int(input("請輸入最小數值"))
# num2 = int(input("請輸入最大數值"))
# ans = random.randint(num1, num2)

# while True:
#     b = int(input("%d到%d數字:" % (num1, num2)))
#     if b > ans:
#         print("再小一點")
#         num2 = b - 1
#     elif b < ans:
#         print("再大一點")
#         num1 = b + 1
#     else:
#         print("恭喜猜中")
#         break

import random

a = random.randint(1, 100)
s = 1
d = 100
while True:
    z = str(s)
    x = str(d)
    i = int(input("請輸入" + z + "~" + x + "的數:"))
    if i == a:
        print("恭喜猜中")
        break
    elif i > a:
        print("再小一點")
        if i > d:
            continue
        elif i < d:
            d = i
        continue
    elif i < a:
        print("再大一點")
        if i < s:
            continue
        elif i > s:
            s = i
