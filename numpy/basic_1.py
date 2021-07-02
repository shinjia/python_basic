# 載入 numpy 套件
import numpy as np

# 根據串列建立 ndarray 物件
ndarray = np.array([3, 5, 4])

print(ndarray)
print(ndarray.ndim)
print(ndarray.size)
print(type(ndarray))
print("---------------------------")


# 建立 ndarray 的幾種方法
ary1 = np.array([1, 2, 3])
ary2 = np.empty(3)  # 未指定內容
ary3 = np.zeros(3)
ary4 = np.ones(3)
ary5 = np.arange(10)

print(ary1)
print(ary2)
print(ary3)
print(ary4)
print(ary5)
print("---------------------------")


# 二維陣列
ary1 = np.array([[1, 2], [3, 4], [5, 6]])
ary2 = np.empty([3, 2])  # 未指定內容
ary3 = np.zeros([3, 2])
ary4 = np.ones([3, 2])

print(ary1.ndim)
print(ary1.size)
print(ary1)
print(ary2)
print(ary3)
print(ary4)
print("---------------------------")


# 三維陣列
ary1 = np.array([[[1, 2, 3, 5], [5, 6, 7, 8], [9, 10, 11, 12]],
                 [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
ary2 = np.empty([2, 3, 4])  # 未指定內容
ary3 = np.zeros([2, 3, 4])
ary4 = np.ones([2, 3, 4])

print(ary1.ndim)
print(ary1.size)
print(ary1)
print(ary2)
print(ary3)
print(ary4)
print("---------------------------")
