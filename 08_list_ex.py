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
# 傳回最大的兩個數 (方法二：用 list 函式排序)
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

a1, a2 = maxtwo(alist)
print("max two is ", a1, ", ", a2)
