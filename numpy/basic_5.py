# numpy 的資料型態

# 匯入 numpy 
import numpy as np


ary1 = np.arange(12).reshape(3,4)

print(ary1)
print(ary1.ndim)
print(ary1.size)
print(ary1.dtype)
print("-----------------------------")


# data type

ary1 = np.array([[1, 2], [3, 4]])
ary2 = np.array([[1.1, 2.2], [3.3, 4]])
ary3 = np.array([['A', 'B'], ['C', 'D']])  # numpy 不是處理字串的

print(ary1.dtype)
print(ary2.dtype)
print(ary3.dtype)

print(type(ary1))  ## python 
print(type(ary2))  ## python 
print(type(ary3))  ## python 
print("-----------------------------")



## numpy 可指定的資料型態
```
- bool  布林型
- int8  8位有符號整數
- int16	 16位有符號整數
- int32	 32位有符號整數
- int64	 64位有符號整數
- uint8  8位無符號整數
- uint16  16位無符號整數
- uint32  32位無符號整數
- uint64  64位無符號整數
- float16	 16位浮點數
- float32 	32位浮點數
- float64  64位浮點數
- complex64  64位複數
- complex128  128位複數
```


# data type assign

ary1 = np.array([[1, 2], [3, 4]])
ary2 = np.array([[1, 2], [3, 4]], dtype='int32')
ary3 = np.array([[1, 2], [3, 4]], dtype='float16')

print(ary1.dtype)
print(ary2.dtype)
print(ary3.dtype)
print("-----------------------------")
