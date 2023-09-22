import random

ans = random.randint(1, 100)
while True:
    x = int(input("請輸入1 ~ 100的整數:"))
    if x == ans:
        print("恭喜猜中")
        break
    elif x < ans:
        print("再大一點")
    elif x > ans:
        print("再小一點")