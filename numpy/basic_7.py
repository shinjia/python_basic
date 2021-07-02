## Matrix 矩陣運算


# 匯入 numpy
import numpy as np


# 一維陣列的內積
ary1 = np.array([1, 2, 3])
ary2 = np.array([4, 5, 6])

ary_result = np.dot(ary1, ary2)
print(ary_result)


# 矩陣運算 (matrix)
data1 = np.array([[2,1]])  # 1x2
data2 = np.array([[3, 2, 1], [3, 1, 4]])  # 2x3

ary1 = data1.dot(data2)  # 內積 1x3
ary2 = data1 @ data2  # 內積 1x3
ary3 = np.outer(data1, data2)  # 外積 2x6

print(ary1)
print(ary2)
print(ary3)
print("----------------------------------")


# 二維陣列 Inner Product

ary1 = np.array([[1, 2, 3], [4, 5, 6]])
ary2 = np.array([[7, 8, 9], [10, 11, 12]])

ary_result = np.matmul(ary1, ary2.T)
print(f'Matrix Product of ary1 and ary2 is:\n{ary_result}\n')

ary_result = np.dot(ary1, ary2.T)
print(f'Dot Product of ary1 and ary2 is:\n{ary_result}\n')

ary_result = (ary1 @ ary2.T)
print(f'arr1 @ ary2 is:\n{ary_result}\n')


# Transpose 轉置矩陣

arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6]])

print(arr1.shape)
print(arr1.T.shape)
print("----------------------------------")

print(arr1 @ arr2.T)
print(arr1.T @ arr2)
print("----------------------------------")
 
 
 