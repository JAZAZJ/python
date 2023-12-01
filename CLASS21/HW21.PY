import random
def roll_dice(n):
    dice = []
    for  i in range(n):
        dice.append(random.randint(1,6))
    return dice 
cnt = int(input("請輸入擲骰子的次數:"))
print(roll_dice(cnt))
