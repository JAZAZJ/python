'''
功能清單
1. 新增科目與成績
2. 刪除某個科目的成績
3. 關閉系統
每回合都要顯示目前的成績以及功能清單
1. 新增科目成績
2. 刪除科目成績
3. 提交所有成績並顯示平均
請輸入功能編號:1
==========================
請輸入想新增的科目:en
請輸入分數:100
==========================
en:100
1. 新增科目成績
2. 刪除科目成績
3. 提交所有成績並顯示平均
請輸入功能編號:1
==========================
請輸入想新增的科目:ch
請輸入分數:aaaaa
輸入錯誤，請重新輸入
請輸入分數:2
==========================
en:100
ch:2
'''

# while True:
#     print("1. 新增科目成績")
#     print("2. 刪除某個科目的成績")
#     print("3. 關閉系統")
#     score_list = ["國語","數學","自然"]
#     print(score_list)
#     num = input("請輸入功能編號:")
#     a = "1"
#     b = "2"
#     c = "3"
#     if num == a:

#         print(score_list[0])
#     elif num == b:
#         num = input("請輸入要移除的科目編號:")
#         d = {"國語": 1, "數學": 2 ,"數學" : 3 }
#         print(score_list[1])
#     elif num == c:
#         print(score_list[2])
#     else:
#         print("關閉系統")
#         break

scores={}
while True:
    print("每回合都要顯示目前的成績以及功能清單")
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    a=input("請輸入功能編號:")
    if a=="1":
        z=input("請輸入想新增的科目:")
        while True:
            try:
                score=int(input("請輸入分數:"))
                break
            except ValueError:
                print("輸入錯誤,請重新輸入")
        scores[z]=score
        print(scores)
    elif a=="2":
        z=input("請輸入想刪除的科目:")
        if z in scores:
            scores.pop(z)
            print("已刪除該科目")
        else:
            print("該科目不存在")
    elif a=="3":
        if not scores:
            print("目前沒有任何成績")
        else:
            total_score=sum(scores.values())
            adg_score=total_score/len(scores)
            print("目前的成績:")
            for subject, score in scores.items():
                print("{}: {}".format(subject, score))
            print("平均成績為：{}".format(adg_score))
            break
    else:
        print("輸入錯誤,請重新輸入")

        