# 練習 Hello World，註解符號

print ("Hello")

"""
單行註解，井字號
大段落文字的註解，三個引號
"""


# 常數，變數 (數字，字串)

a = 7
b = 3
c = a * b
print(a, "*",   b, "=", c)
print (7%3)
name = "Vincent "
print("My name is ", name)


# 運算 + - * / % **，注意資料型態
print ("3*3....", 3**2)
print (pow(4,2))


# 函式呼叫
a = 10
b = 3
c = round(a/b, 2)
d = int(c)
print ("round...", c)
print ("int...", d)

# import 特殊函式庫 (math, time, random)

import math
x = math.sqrt(5)
print ("x=", x)


import time
t = time.time()
print("current time...", t)
print(time.localtime(time.time()))
print(time.localtime(time.time()).tm_year)

import random
print("random number ", random.random())
print("random number ", math.floor(random.random()*10))  # 0...9
print("random number ", math.floor(random.random()*10)+1)  # 1...10

# a..b (random number, int)
# floor(random() * (b-a+1)) + a

print("random number ", random.randint(1,6))
print("random number ", random.randrange(1, 7))


# 條件判斷句 (冒號，tab縮格)
a = random.randint(1,6)
print("-----------------")
print("a=", a)
if a>=5:
    print("BIG")
    print("BIG")
elif a>=3:
    print("Middle")
    print("Middle")
else:
    print("SMALL")
    print("SMALL")


# 關係運算子 == > >= < <= !=
# 邏輯運算子 and or not
# 布林值 True False
a = 6
b = 7
if (a!=3 and b==7):
    print("ok")

if(not False):
    print("True")



# 迴圈句型 while (沒有 do--while語法)
# 範例: 丟一個骰子，直到出現6時停止，計算次數
dice = random.randint(1,6)
cnt = 0
while dice!=6:
    print(dice)
    cnt = cnt + 1
    dice = random.randint(1,6)

print ("cnt=", cnt, "   dice=", dice)

# 丟一個骰子，直到連續兩個相同後停止
a = -1
b = random.randint(1,6)
while not (a==b):
    a = b
    b = random.randint(1,6)
    print ("dice: ", a, ",", b)

print ("end")


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



# 函式定義與呼叫
# 範例：計算從a加到b，用自定函式 (含預設值用法)
def sumab(a, b=10):
    s = 0
    for i in range(a, b+1):
        s = s + i
    return s


print("--------------------")
ans = sumab(1)
print("sum=", ans)



# 串列 list (Python無陣列)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('banana'))

fruits.append("西瓜")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(len(fruits))


# 範例：傳入一個串列，定義一個函式，傳回最大的前兩個數 (包含重覆)
'''
# 傳回最大的數
def maxtwo(listdata):   
    maxvalue = -99999  # 先指定成為一個最小小小的數
    for i in range(0, len(listdata)):
        if listdata[i] > maxvalue:
            maxvalue = listdata[i]
    return maxvalue, 0

'''

'''
# 傳回最大的兩個數 (方法一)
def maxtwo(listdata):   
    max1 = -99999  # 先指定成為一個最小小小的數
    max2 = -99999
    for i in range(0, len(listdata)):
        if listdata[i] > max1:
            max2 = max1
            max1 = listdata[i]
        elif listdata[i] > max2:
            max2 = listdata[i]
        print(i, ", ", listdata[i], "===" , max1, ",", max2)
            
    return max1, max2

'''
''' 傳回最大的兩個數 (方法二：用list函式排序)
def maxtwo(listdata):   
    listdata.sort()
    listdata.reverse()
    return listdata[0], listdata[1]

'''

def maxtwo(listdata):   
    listdata.sort()
    listdata.reverse()
    return listdata[0], listdata[1]


alist = [5, 2, 4, 1, 7, 9, 8, 6, 3]

print("---------------------------")
a1, a2 = maxtwo(alist)
print("max two is ", a1, ", ", a2)

