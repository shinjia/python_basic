# 匯入 numpy
import numpy as np


## 指定與複製


ary = np.array([1, 2, 3])

ary1 = ary
ary2 = ary.copy()

ary[0] = 9
# ary[:] = 9
# ary *= -1
# ary = ary * -1  ## 這個很不一樣

print(ary)
print(ary1)
print(ary2)
print("-----------------------------")


## 合併資料


# concatenate
# 擴展 (維度不變)

x1 = np.array([[1, 2, 3], [4, 5, 6]])
x2 = np.array([[-1, -2, -3], [-4, -5, -6]])

ary1 = np.concatenate((x1, x2), axis=0)  ## 可以更多個
ary2 = np.concatenate((x1, x2), axis=1)

print(ary1)
print(ary2)
print(x1.shape)
print(ary1.shape)
print(ary2.shape)
print("-----------------------------")


# stack
# 堆疊，會增加維度

x1 = np.array([[1, 2, 3], [4, 5, 6]])
x2 = np.array([[-1, -2, -3], [-4, -5, -6]])

ary1 = np.stack((x1, x2), axis=0)  ## 可以更多個堆疊
ary2 = np.stack((x1, x2), axis=1)
ary3 = np.stack((x1, x2), axis=2)
ary4 = np.stack((x1, x2), axis=-1)

print(ary1)
print("-----------------------------")
print(ary2)
print("-----------------------------")
print(ary3)
print("-----------------------------")
print(ary4)
print("-----------------------------")
print(x1.shape)
print(ary1.shape)
print(ary2.shape)
print(ary3.shape)
print(ary4.shape)
print("-----------------------------")


# vstack, hstack
# 建議用平面二維(或三維)去思考
# vstack: 垂直合併
# hstack: 水平合併

x1 = np.array([[1, 2, 3], [4, 5, 6]])
x2 = np.array([[-1, -2, -3], [-4, -5, -6]])

ary1 = np.vstack((x1, x2))
ary2 = np.hstack((x1, x2))

print(ary1)
print("-----------------------------")
print(ary2)
print("-----------------------------")


# 切割

# 切割一維陣列

x1 = np.arange(30)
n = 7
ary = np.array_split(x1, n)

# print(ary)
for x in ary:
  print(x)

print("-----------------------------")


# 切割二維陣列

x1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
n = 2
ary = np.array_split(x1, n)

print(ary)
# 切割後的資料型態為 numpy.ndarray 的 list (所以不能用 ary.shape 查看)
print(type(ary))
print(type(ary[0]))

for x in ary:
  print(x)

print("-----------------------------")


# 指定 axis
x1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
n = 2

ary = np.array_split(x1, n)
ary1 = np.array_split(x1, n, axis=0)
ary2 = np.array_split(x1, n, axis=1)

for x in ary2:
  print(x)

print("-----------------------------")


# vsplite, hsplite
x1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
n = 2

ary = np.array_split(x1, n)
ary1 = np.vsplit(x1, n)
ary2 = np.hsplit(x1, n)

for x in ary1:
  print(x)

for x in ary2:
  print(x)

print("-----------------------------")
