'''
歡迎使用點餐機！請選擇您想要的功能(輸入數字)：
1. 新增餐點到點餐清單
2. 從點餐清單中移除特定餐點
3. 在指定位置加入餐點
4. 計算點餐清單中某餐點的數量
5. 取消點餐清單中的最後一項餐點
6. 取消點餐清單中特定位置的餐點
7. 顯示升序排序的點餐清單
8. 顯示降序排序的點餐清單
9. 反轉點餐清單的順序
10. 查詢餐點在點餐清單中的位置
11. 退出點餐機
'''
# order_list = []
# while True:
#     print("歡迎使用點餐機！")
#     food = ["雞塊", "薯條", "漢堡", "可樂"]

while True:
    food = ["漢堡", "薯條", "雞塊", "系統關閉"]
    print("歡迎使用點餐機！")
    print(food)
    num = input("請輸入編號:")
    a = "0"
    b = "1"
    c = "2"
    d = "3"
    if num == a:
        print(food[0])
    elif num == b:
        print(food[1])
    elif num == c:
        print(food[2])
    elif num == d:
        print(food[3])
        break
    else:
        print("輸入錯誤查無此餐點，請重新輸入")
