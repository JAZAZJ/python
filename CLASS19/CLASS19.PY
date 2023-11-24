# d = {1: "a", 2:"b"}
# values = d.values()# 'a', 'b'
# for value in values:
#     print(value)

# d = {1: "a",2: "b"}  
# items = d.items()
# for item in items:
#     print(item)
#     print(item[1],item[0])

# d = {1:"a",2:"b"}
# items = d.items()
# """
# (1, "a")
# (2, "b)
# """

# for key,value in items: 
#     print(key,value)

# food_list = {"蛋糕": 1,"三明治":10,"果汁":20,"薯條": 15, "披薩": 2 }
# for food, count in food_list.items():
#     if food == "果汁":
#         print(food + ":" + str(count) + "杯" )
#     else:
#         print(food + ":" + str(count)+"份")

# book = {}
# book["書名"] = "嗨"
# book["作者"] = "gg"
# print(book)

# food_list = {"蛋糕": 1,"三明治":10,"果汁":20,"薯條": 15, "披薩": 2 }
# food_list["冰淇淋"] = 10
# food_list["熱狗"] = 20
# food_list["果汁"] = 25

# for food, count in food_list.items():
#     if food == "果汁":
#         print(food + ":" + str(count) + "杯" )
#     else:
#         print(food + ":" + str(count)+"份")

d = {1: 'a', 2: 'b'}
keys = d.keys()
for a in keys:
    print(a)