# 函式呼叫
a = 10
b = 3
c = a / b
x1 = round(a/b, 2)
x2 = int(c)
print("round...", x1)
print("int...", x2)


# 函式定義與呼叫
def add(a, b):
    result = a + b
    return result

print("--------------------")
x1 = add(3, 7)
print(x1)


# 範例：計算從a加到b，用自定函式 (含預設值用法)
def sumab(a, b=10):
    s = 0
    for i in range(a, b+1):
        s = s + i
    return s

print("--------------------")
x1 = sumab(1)
print(x1)
