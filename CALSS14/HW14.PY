import random

num1 = int(input("請輸入最小數值"))
num2 = int(input("請輸入最大數值"))
ans = random.randint(num1, num2)

while True:
    b = int(input("%d到%d數字:" % (num1, num2)))
    if b > ans:
        print("在小一點")
    elif b < ans:
        print("再大一點")
        num1 = b + 1
    else:
        print("恭喜猜中")
        break