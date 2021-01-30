# 函式呼叫
a = 10
b = 3
c = a / b
x1 = round(a/b, 2)
x2 = int(c)
print("round...", x1)
print("int...", x2)


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
