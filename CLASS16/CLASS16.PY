# l = ["a", "b", "c"]
# print(l)
# l[0] = "A"
# # print(l)
# waether = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
# print(waether)
# while True:
# try:
#     ans = int(input("請輸入要修改的星期數字(1~7):"))
# except:
#     print("請輸入數字編號")
# else:
#     if ans > len(waether) or ans < 1:
#         print("請重新輸入")
#     else:
#         print("原本的天氣是" + waether[ans - 1])
#         new_weather = input("請輸入新的天氣:")
#         waether[ans - 1] = new_weather
#         print("你修改後的天氣是" + waether[ans - 1])
#         print(waether)
#         break
# a = [1, 2, 3]
# b = b[0] = 2
# print(a)
# l = ["a", "b", "c"]
# a = l.copy()
# a[0] = 1
# print(a, l)
# fruit_list = ["火龍果", "哈密瓜", "百香果", "橘子"
#               "蘋果", "香蕉", "梨", "李", "桃"]
# print("最長的水果名稱是" + max(fruit_list))
# print("最短的水果名稱是" + min(fruit_list))
# birthday = "2023/10/20"
# birthday = birthday.split("2")
# print(birthday)
# birthday = "+".join(birthday)
# print(birthday)
# img = ["2023", "10", "20"]
# x = '-'.join(img)
# print(x)