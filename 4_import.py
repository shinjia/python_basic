# import 特殊函式庫 (math, time, random)

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
