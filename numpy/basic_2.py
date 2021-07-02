# ndarray 基礎運算功能
# - 數字運算
# - 逐元運算 (elementwise)
# - 矩陣運算 (matrix)
# - 統計運算 (statistics)

import numpy as np


# 數字運算
data1 = np.array([3, 2, 6])
data2 = np.array([4, 7, 2])
ary1 = data1 + 10
ary2 = data1 - 10
ary3 = data1 * 10
ary4 = data1 / 10
print(ary1)
print(ary2)
print(ary3)
print(ary4)
print("----------------------------------")


# 逐元運算 (elementwise)
data1 = np.array([3, 2, 6])
data2 = np.array([4, 7, 2])

ary1 = data1 + data2
ary2 = data1 - data2
ary3 = data1 * data2
ary4 = data1 / data2
ary5 = data1 > data2
ary6 = data1 == data2
ary7 = data1 <= data2
print(ary1)
print(ary2)
print(ary3)
print(ary4)
print(ary5)
print(ary6)
print(ary7)
print("----------------------------------")

# 問題：
# (1) 若是二維和二維的運算呢？
# (2) 若是二維和一維的運算呢？
# (3) 反之，若是一維和二維的運算呢？


# 矩陣運算 (matrix)
data1 = np.array([[2,1]])  # 1x2
data2 = np.array([
    [3, 2, 1], [3, 1, 4]
])  # 2x3
ary1 = data1.dot(data2)  # 內積 1x3
ary2 = data1@data2  # 內積 1x3
ary3 = np.outer(data1, data2)  # 外積 2x6

print(ary1)
print(ary2)
print(ary3)
print("----------------------------------")


# 統計運算 (statistics) 單元運算
data = np.array([
    [2, 1, 5], 
    [3, 4, 2]
])

ary1 = data.sum()  # 全部加總
ary2 = data.sum(axis=0)  # 加總 column
ary3 = data.sum(axis=1)  # 加總 row
ary4 = data.max()  # 全部最大值
ary5 = data.min()  # 全部最小值
ary6 = data.mean()  # 平均數
ary7 = data.std()  # 標準差
ary8 = data.cumsum()  # 逐值累加
print(ary1)
print(ary2)
print(ary3)
print(ary4)
print(ary5)
print(ary6)
print(ary7)
print(ary8)
print("----------------------------------")
