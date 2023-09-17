# i = 0
# while i < 5:
#     print(i)
#     i = i + 1

# for i in range(5):
# print(i)
# += 加法 a += 2 a = a + 2 結果102
# -= 減法 a-=3. a = a - 3. 結果 97.0
# += 乘法 a+= 4 a=a - 3. 結果 400
# /= 小數除法 a/= 4 a=a / 4
# //= 整數除法 a//=4 a=a //4
# %= 取餘數 a%=4 a=a % 4
# **= 次方 a**=4 a=a ** 4

# 運算子順序 1.()括號
# 2.**次方
# +(正數) -(負數)
# *乘法 除法/ %(餘數) //(取商)
# +(加法) -(減法)
# == != > < >= <=
# not and or
# = += -= *= /= %= //= **=

# ans = ''
# while ans != "1234":
#     ans = input("請輸入密碼:")
#     if ans != "1234":
#         print("密碼錯誤,請重新輸入")

# print("歡迎光臨")

Sum = 0
price = int(input("請輸入商品金額:"))
while price != 0:
    Sum += price
    print("目前金額為" + str(Sum) + "元")
    price = int(input("請輸入商品金額"))

# x = int(input("請輸入正整數:"))
# if x == 1:
#     print(f"{x}不是質數")
# else:
#     i = 2
#     while x % i != 0 and i != x:
#         i += 1
#     if i == x:
#         print("yes")
#     else:
#         print("no")
