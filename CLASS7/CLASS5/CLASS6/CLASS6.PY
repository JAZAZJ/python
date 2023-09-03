# 程式發生錯誤就停止運作了怎麼辦
# EX: 如果這時候使用者輸入的不是數字就會發生錯誤並離開程式

try:
    num = int(input("請輸入一個數字"))
    total = num + 1
    print(total)
except:
    print("發生錯誤")
#    ==      相等       1==1   Ture
#    !=      不相等     1!=0   ture
#    >=      大於等於   1>=2   False
#    <=      小於等於   1<=2   ture
#    >       大於       1>2   False
#    <       小於       1>2   ture
# 比較運算子  運轉       範例   結果(布林)
