# 一組資料
# 注意：Python無陣列
# - 可變串列 List：有順序，可變動的資料集合 (使用中括弧)
# - 固定串列 Tuple：有順序，不可變動的資料集合 (使用小括弧)
# - 集合 Set：無順序的資料集合 (使用大括弧)
# - 字典 Dictionary：kay-value 的集合，例如 {"apple":"蘋果"}


# 串列 List
score = [45, 93, 53, 63, 72, 88]
score[0] = 23
print(score)

x1 = score[1:4]  # 不包含結尾
print(x1)

score[1:4] = []  # 直接更改 list 的資料 (此處為刪除部分的 list)
print(score)

score = score + [12, 33] # list 的串接
print(score)

print("================================")

# 多維串列 (巢狀)
data = [[1,2,3], [4,5,6]]
print(data)
print(data[0][0:2])

print("================================")

# 串列 List 的運算

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print(len(fruits))
print(fruits.count('apple'))
print(fruits.index('banana'))

fruits.append("西瓜")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(len(fruits))

# --------------------------------------

# Tuple
data = (4, 5, 2, 6)
print(data)
