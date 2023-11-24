'''
hw15
請將hw13的作業升級
• 請將果汁新增到list並使用list完成之前的功能
juices_list = ["蘋果汁","柳橙汁","葡萄汁","系統關閉"]
'''
# juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]
# print(juices_list)
while True:
    
    juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]
    print(juices_list)
    num = input("請輸入編號:")
    a = "1"
    b = "2"
    c = "3"
    d = "4"
    if num == a:
        print(juices_list[0])
    elif num == b:
        print(juices_list[1])
    elif num == c:
        print(juices_list[2])
    elif num == d:
        print(juices_list[3])
        break
    else:
        print("輸入錯誤查無此果汁，請重新輸入")
