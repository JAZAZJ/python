# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# 輸入要跳繩的次數
# jump = int(input("請輸入要跳繩的次數:"))
# 跳繩
# for i in range(1, jump + 1):
#     if i % 10 == 0:
#         print("休息一下")
#         continue
#     print("第" + str(i) + "次跳繩")

# random.randrange可跳數,但不能做到結尾
# random.randint 不可跳數但可做到結尾
import random

# random.randrange(3)
# print(random.randrange(3))

# random.randrange(3)
# print(random.randrange(19999))

# random.randrange(178)
# print(random.randrange(1999955))

# print(random.randint(1, 59))
# print(random.randint(1, 100))
# import random as X

# print(X.randint(i, 10))
# import random

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