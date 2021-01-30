
# 一組資料
# - 可變串列 List：有順序，可變動的資料集合 (使用中括弧)
# - 固定串列 Tuple：有順序，不可變動的資料集合 (使用小括弧)
# - 集合 Set：無順序的資料集合 (使用大括弧)
# - 字典 Dictionary：kay-value 的集合，例如 {"apple":"蘋果"}


# 串列 list (Python無陣列)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('banana'))

fruits.append("西瓜")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(len(fruits))


# 範例：傳入一個串列，定義一個函式，傳回最大的前兩個數 (包含重覆)
'''
# 傳回最大的數
def maxtwo(listdata):   
    maxvalue = -99999  # 先指定成為一個最小小小的數
    for i in range(0, len(listdata)):
        if listdata[i] > maxvalue:
            maxvalue = listdata[i]
    return maxvalue, 0

'''

'''
# 傳回最大的兩個數 (方法一)
def maxtwo(listdata):   
    max1 = -99999  # 先指定成為一個最小小小的數
    max2 = -99999
    for i in range(0, len(listdata)):
        if listdata[i] > max1:
            max2 = max1
            max1 = listdata[i]
        elif listdata[i] > max2:
            max2 = listdata[i]
        print(i, ", ", listdata[i], "===" , max1, ",", max2)
            
    return max1, max2
'''

'''
# 傳回最大的兩個數 (方法二：用list函式排序)
def maxtwo(listdata):   
    listdata.sort()
    listdata.reverse()
    return listdata[0], listdata[1]
'''

def maxtwo(listdata):   
    listdata.sort()
    listdata.reverse()
    return listdata[0], listdata[1]


alist = [5, 2, 4, 1, 7, 9, 8, 6, 3]

print("---------------------------")
a1, a2 = maxtwo(alist)
print("max two is ", a1, ", ", a2)

# --------------------------------------
