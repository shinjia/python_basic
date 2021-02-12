# 迴圈句型 while (沒有 do--while語法)
# 範例: 丟一個骰子，直到出現6時停止，計算次數

import random

dice = random.randint(1,6)
cnt = 0
while dice!=6:
    print(dice)
    cnt = cnt + 1
    dice = random.randint(1,6)

print("cnt=", cnt, "   dice=", dice)


# 丟一個骰子，直到連續兩個相同後停止
a = -1
b = random.randint(1,6)
while not (a==b):
    a = b
    b = random.randint(1,6)
    print ("dice: ", a, ",", b)

print("end")


# 迴圈 for
# range()三種傳入參數的意義
print("----------------------------------------")
print("      1   2   3   4   5   6   7   8   9 ")
print("----------------------------------------")
for i in range(1, 10): 
    print(i, "|  ", end="")
    for j in range(1, 10):
        print(format(i*j, "2d"), " ", end="")
    print("")
print("----------------------------------------")
