# 字串型態與運算

# 字串的表示 (單引號或雙引號)
x1 = "Hello"
x2 = "Hell\"o"
x3 = 'Hello'
x4 = 'Hell\'o'
x5 = 'Hell"o'
x6 = "Hello\nWorld"  # 換列

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)


"""
Hello World 111
可以寫多列文字
"""  # 多列文字，注意此處未被指定，則為註解

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

print(x7)
print(x8)


# 字串長度

x1 = '1234'
x2 = '中文字'
x3 = 'OK你好'
x4 = '12\n\n34'
x4 = '12\n\n34'
x5 = r'12\n\n34'  # 保留原始樣式

print(len(x1))
print(len(x2))
print(len(x3))
print(len(x4))
print(len(x5))


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
x1 = s[0]   # 稱做第零個字元
x2 = s[1:4]  # 開頭和結束 (包含開頭，不包含結尾)
x3 = s[1:]  # 取到最後面
x4 = s[:4]  # 注意不包含結尾
x5 = s[-1]  # 從最後算起
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
