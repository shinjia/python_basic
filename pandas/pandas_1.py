import pandas as pd

# Series 單維度的資料
srcList = [1, 5, 2, 6, 3, 8]
data = pd.Series(srcList)

print(data.max())  # 最大值
print(data.median())  # 中位數

data = data * 2  # 各值乘以兩倍
print(data)

data=data==10
print(data)
print("----------------------------")


# DataFrame 雙維度的資料
srcDict = {
    "name":["Allen", "Ariel", "Angel"],
    "age" :[3000, 2000, 5000]
}
print(srcDict)

data = pd.DataFrame(srcDict)
print(data)

print(data["name"])  # 取得特定的欄位
print(data.iloc[0])  # 取得特定的列