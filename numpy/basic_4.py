## numpy 的 index

# 匯入 numpy
import numpy as np


# 索引

ary = np.arange(8)

print(ary)
print(ary[1:5])
print(ary[:4])
print(ary[3:])
print(ary[-4:-1])
print(ary[0:8:2])
print(ary[::2])
print("-----------------------------")


# 二維陣列

ary = np.arange(20).reshape(4,5)

print(ary)
print(ary[1:3, 1:-1])
print("-----------------------------")


## 陣列的走訪

# 讀取各個元素 (for..in)

ary = np.array([[1, 2, 3], [4, 5, 6]])

# 練習一
for x in ary:
  print(x)
  print('---')

print("-----------------------------")

# 練習二
for x in ary:
  for y in x:
    print(y)

print("-----------------------------")

# 練習三
for x in ary.reshape(6):
  print(x)

print("-----------------------------")


# 讀取各個元素 (nditer, ndenumerate)

ary = np.array([[1, 2, 3], [4, 5, 6]])

# 練習四
for x in np.nditer(ary):
  print(x)

print("-----------------------------")

# 練習五
for x in np.ndenumerate(ary):
  print(x)

print("-----------------------------")

# 練習六
for i, x in np.ndenumerate(ary):
  print(i, x)

print("-----------------------------")


## 陣列走訪速度比較

import time

# 速度比較一
ary = np.zeros((3000,2000,3))

t1 = time.time()
for x in ary:
  for y in x:
    for z in y:
      # do nothing
      a = z

t2 = time.time()
print(t2-t1)


# 速度比較二
ary = np.zeros((3000,2000,3))

t1 = time.time()
for x in np.nditer(ary):
  # do nothing
  a = z

t2 = time.time()
print(t2-t1)


# 速度比較三
ary = np.zeros((3000,2000,3))

t1 = time.time()
a = ary[:,:,:]
t2 = time.time()
print(t2-t1)
