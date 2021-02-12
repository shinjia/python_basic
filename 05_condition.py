# 條件判斷句 (冒號，tab縮格)
# Python 不支援 switch 語法

import random

a = random.randint(1,6)
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
if(a!=3 and b==7):
    print("ok")

if(not False):
    print("True")
