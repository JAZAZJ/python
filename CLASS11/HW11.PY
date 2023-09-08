"""作業1
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
hint:可以使用%取餘數進行判斷
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""
"""
作業2
請輸入要印出的箭頭大小
hint:
可利用字串乘法
>>>val="*" * 3
>>>print(val)
>>>***
EX:
請輸入要印出的箭頭大小:3
  *
 ***
*****
  *
  *
  *
"""
# homework 1
num = int(input("請輸入一個正整數"))
for num in range(1, num):
    i = num % 3
    x = num % 7
    if (i and x) == 0:
        print(num)

# homework 2
# num = int(input("請輸入要印出的箭頭大小"))
# for i in range(1, num + 1):
#     print(' ' * (num - i) + '*' * (2 * i - 1))  # +號左邊印出空格,+號右邊印出星星
# for j in range(1, num + 1):
#     print(' ' * (num - 1) + '*')
