# "判斷字典裡有沒有該鍵"
# "如果有責回傳Ture"
# "如果沒有則回傳False"
# d = {1:"a",2:"b"}
# 1 in d
# "A" in d
# "a" in d
# print(2 in d) 

# food_list = {"蛋糕": 1,"三明治":10,"果汁":20,"薯條": 15, "披薩": 2 }
# food_list["冰淇淋"] = 10
# food_list["熱狗"] = 20
# food_list["果汁"] = 25
# parent_food_list = {"蛋糕": 1,"三明治":10,"果汁":20,"薯條": 15, "披薩": 2 }
# for food, count in food_list.items():
#     if food == "果汁":
#         print(food + ":" + str(count) + "杯" )
#     else:
#         print(food + ":" + str(count)+"份")
# print("還須購買的食物及數量:")
# for food ,count in food_list.items():
#     if not (food in parent_food_list):
#         print(food + ":" + str(count)) 
#     elif food in parent_food_list and parent_food_list[food] < count:
#         print(food +":" + str(count == parent_food_list[food]))

# pop 1 
# 移除指定鍵的資料(必須存在)
# 返回被移出的資料區
# d = {1: "a",2: "b", 3:"c"} 
# v = d.pop(2)
# print("更新後的字典",d) 
# print("移出的數值:", v)

# pop 2 
# 嘗試移出指定鍵的資料
# 如果鍵不存在,返回預設值
# d = {1: "a", 2: "b"}
# v = d.pop(0,"刪除資料失敗") 
# print("更新後的字典:", d)
# print("移除的數值", v)

# food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
# food_list["冰淇淋"] = 10
# food_list["熱狗"] = 20
# food_list["果汁"] = 25
# # 派對後剩下的食物和數量  
# remaining_food = {"蛋糕": 0, "三明治": 5, "果汁": 8, "薯條": 10, \
#                 "披薩": 1, "冰淇淋": 3, "熱狗": 0}
# # 更新食物列表並移除已經吃完的食物
# for food, count in remaining_food.items():
#     if count == 0:
#         food_list.pop(food, None)
#         print(food + "已經吃完")
#     else:
#         food_list[food] = count
# for food, count in food_list.items():
#     if food == "果汁":
#         print(food + ": " + str(count) + "杯")
#     else:
#         print(food + ": " + str(count) + "份")

# len 在字典裡能算有幾個key
# food_list = {"蛋糕": 1, "三明治": 10, "果汁": 20, "薯條": 15, "披薩": 2}
# print(len(food_list))
# food_list["冰淇淋"] = 10
# food_list["熱狗"] = 20
# food_list["果汁"] = 25
# print(len(food_list))

gifts = {"小名":"積木","小花":"畫筆","小強":"足球","小美":"書","小偉":"遙控車"}
# 顯示一共收到幾個禮物
print("一共收到了" + str(len(gifts)) + "個禮物")
for name,gift in gifts.items():
    print(name + "送了你一個" + gift)