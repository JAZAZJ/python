# not  邏輯
# and  邏輯
# or   邏輯
# not ture (False)
# not False (ture)
# 運算子優先順序
# 1 ()括號
# 2 **次方
# 3 +(正數) -(複數)
# 4 *(乘法) /(除法) %(餘數) //(取商)
# 5 == != > < >= <=
# 6 not and or
# if敘述
# else敘述
# 當判斷式為真,執行程式的指令
# 當判斷式為真,跳過不執行
# 當判斷式為真,執行 if 區塊內的指令
# 當判段式為假,執行 else 塊內的指令
passworld= input("請輸入密碼")
if passworld == "1234":
    print("歡迎光臨john")
elif passworld-=="5678":
    print("歡迎Ray")
else:
    print("密碼錯誤")