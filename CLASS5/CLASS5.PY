name = "python"
age = 1000
print("我叫做" + name + "我今年" + str(age) + '歲了!')
# %s 代表字串的變數
# %f 代表小數的變數
# %d 代表整數的變數
# print("我是%s,我今年%d歲了!" % (name, age))
# 請輸入你想知道python幾年後的年齡: 10
age = input("請輸入python的年齡")
age = int(age) + 10
print(age)