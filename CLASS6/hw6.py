"""
有一個國家B的氣溫，永遠只有A國家的一半又多5度，那你們每次輸入A國家的氣溫，就要顯示B國家現在幾度！
EX:
請輸入A國家溫度:61
A國溫度61.0度，B國家現在溫度35.5度
請輸入A國家溫度:ABC
輸入錯誤!
"""
try:
    num = int(input("請輸入A國家溫度"))
    total = num // 2 + 5
    print(total)
except:
    print("輸入錯誤")
