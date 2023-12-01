# import random
# a = int(input("請輸入擲骰子的次數:"))
# x = random.randint(1,6)
# print(x)
# while x != a:
#     x = random.randint(1,6)
#     print(x)

# import random

# x = int(input("請輸入擲骰子的次數:"))
# def count(i,time):
#     results = []
#     for i in range(1,x):
#         print(random.randint(1, 6))


import random
x = int(input("請輸入擲骰子的次數:"))
for i in range(x):
    print(random.randint(1, 6))