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


# 無限參數 (可以有不定數量的參數)
def show(*msgs):
    print(msgs)  ## 取得 Tuple 的資料
    for msg in msgs:
        print(msg)
    return

show("Hello", "World", "Python")


# 範例：計算一些數字的平均
def avg(*nums):
    sum = 0
    for n in nums:
        sum += n
    result = sum / len(nums)
    return result
    
x1 = avg(1, 2, 3, 4, 5)
x2 = avg(3, 1, 2)
print(x1)
print(x2)