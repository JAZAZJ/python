# 使用者輸入一個數字 X
# 計算由 0 + 1...+ X 的總和,並將總和顯示出來
# x = int(input("請輸入一個整數:"))
# Sum = 0
# for i in range(x + 1):
#     Sum = Sum + i
# Sum = str(Sum)
# x = str(x)
# print("從0加到" + x + "的總合為" + Sum)
for i in range(1, 10):
    for j in range(1, 10):
        i = int(i)
        Sum = j * i
        i = str(i)
        j = str(j)
        Sum = str(Sum)
        print(j + "*" + i + "=" + Sum)
