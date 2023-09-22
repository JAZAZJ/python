while True:
    print("1.蘋果汁")
    print("2.柳橙汁")
    print("3.葡萄汁")
    print("4.系統關閉")
    num = input("請輸入編號:")
    a = "1"
    b = "2"
    c = "3"
    d = "4"
    if num == a:
        print("您點的商品是蘋果汁")
    elif num == b:
        print("您點的商品是柳橙汁")
    elif num == c:
        print("您點的商品是葡萄汁")
    elif num == d:
        print("系統關閉")
        break
    else:
        print("輸入錯誤查無此果汁，請重新輸入")
