'''
判斷輸入成績的等第
使用者輸入成績
顯示使用者的等第
成績等第
A : 90 以上
B : 80 分到 89 分
C : 70 分到 79 分
D : 60 分到 69 分
E : 59 分以下
ex:
例如:使用者輸入成績50 顯示E。使用者輸入62則顯示D
'''
score = input("請輸入成績")
if score >= "90":
    print("你的等級為A")
elif score >= "80" and score <= "89":
    print("你的等級為B")
elif score >= "70" and score <= "79":
    print("你的等級為C")
elif score >= "60" and score <= "69":
    print("你的等級為D")
else:
    score <= "59"
    print("你的等級為E")