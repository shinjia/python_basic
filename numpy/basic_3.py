# 多維陣列的形狀 Shape
# 維度：資料的層次
# 形狀：同時表達資料的層次，和每個層次的資料數量

import numpy as np

data1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # 形狀 (8,)

data2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])  # 形狀 (2, 4)

data3 = np.array([
    [ [1, 2], [3, 4] ],
    [ [5, 6], [7, 8] ]
])  # 形狀 (2, 2, 2)

print(data1.shape)
print(data2.shape)
print(data3.shape)
print("-----------------------------")


# 資料轉置
data = data2
print(data.shape)
print(data.T.shape)
print(data.T)
print("-----------------------------")


# 扁平化資料：把多維的資料打平成一維職列
data = data3
print(data.ravel())


# 重塑資料形狀：改變資料的形狀，資料的總數量必須要一樣
data = np.arange(0, 8)

print(data)
print(data.reshape(2, 4))
print(data.reshape(4, 2))
print(data.reshape(2,2,2))
print(np.zeros(18).reshape(3,6))
print(np.zeros(18).reshape(2,3,3))

