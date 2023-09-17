import time
# 輸入秒數
second = int(input("請輸入秒數: "))
# 倒數計時
for i in range(second, 0, -1):
    print(i)
    time.sleep(1)
else:
    print("時間到!")