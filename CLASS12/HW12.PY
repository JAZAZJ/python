'''
HW12:
輸入一組整數範圍，將範圍中的所有質數顯示於畫面上。
EX：
請輸入開始整數:10
請輸入結束整數:50
11
13
17
19
23
29
31
37
41
43
47
'''
# b = int(input("請輸入開始整數"))
# a = int(input("請輸入結束整數"))
# ans = False
# if a == 1:
#     print("1不是質數")
# else:
# for i in range(2, int(a / 2 + 1)):
#     if a % i == 0:
#         ans = True
# if ans == True:
#     print(str(a) + "不是質數")
# else:
#     print(str(a) + "是質數")

# x = int(input("請輸入開始整數:"))
# y = int(input("請輸入結束整數:"))

# for i in range(x, y + 1):
#     if (x < 2):
#         print(x, "不是質數,即將跳出程式")
#         break
#     j = 2
#     count = 0
#     while j < i:
#         if (i % j == 0):
#             count = 1
#         j = j + 1
#     if (count == 0):
#         print(i)

a = int(input("請輸入起始數值"))
b = int(input("請輸入終值數值"))
for i in range(a, b):
    statu = False
    if i > 1:
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                statu = True
    if statu == False and i != 1:
        print(i)
