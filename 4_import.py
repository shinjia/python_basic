# 模組 module
# 獨立的程式檔案，此檔案可以被重覆載入使用

# import 模組
# 載入
# - import 模組名稱
# - import 模組名稱 as 模組別名
# 使用
# - 模組名稱或別名.變數名稱
# - 模組名稱或別名.函式名稱

# 內建模組 (例如：math, time, random)

import sys
print(sys.platform)
print(sys.maxsize)  # 整數型態的最大值
print(sys.path)  # 搜尋模組的路徑

sys.path.append("modules")

import sys as s
print(s.platform)
print(s.maxsize)
print(s.path)


import math
x = math.sqrt(5)
print("x=", x)


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
