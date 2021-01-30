# 資料型態與常數，變數
#  - 數字：整數、長整數、浮點數
#  - 字串 (單引號或雙引號)
#  - 布林值 (True, False)


# 運算 + - * / % **，注意資料型態
a = 7
b = 3
x1 = a + b
x2 = a - b
x3 = a * b
x4 = a / b
x5 = a // b  # 整數除法
x6 = a % b   # 整數除法的餘數
x7 = a ** b  # 次方
x8 = pow(a, b)  # 使用函式 
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)
print(x8)


# 字串的表示
x1 = "Hello"
x2 = "Hell\"o"
x3 = 'Hello'
x4 = 'Hell\'o'
x5 = 'Hell"o'
x6 = "Hello\nWorld"  # 換列
x7 = """
Hello
World
可以寫多列文字
"""  # 多列文字，注意此處頭尾都多加上換列
x8 = '''
Hello
World
可以寫多列文字
'''  # 多列文字，注意此處頭尾都多加上換列
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)
print(x8)


# 字串的運算
x1 = "Hello" + "World"
x2 = "Hello" "World"  # 使用空白也代表字串串接
x3 = "Hello"*3  ## 重覆幾次
x4 = "Hello"*3+"World"
print(x1)
print(x2)
print(x3)
print(x4)


# 字串中字元的操作
# 字串中每個字元都有編號索引，由 0 開始
s = "HelloWorld"
x1 = s[0]
x2 = s[1:4]  # 開頭和結束 (包含開頭，不包含結尾)
x3 = s[1:] 
x4 = s[:4]  # 注意不包含結尾
print(x1)
print(x2)
print(x3)
print(x4)
