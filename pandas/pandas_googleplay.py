import pandas as pd

data = pd.read_csv("googleplaystore.csv")
print(data)
print("---------------------------------")

print("資料數量", data.shape)
print("資料欄位", data.columns)
print("---------------------------------")

# condition = data["Rating"]>5
# data = data[condition]
# print(data)

condition = data["Rating"]<=5
data = data[condition]

print("平均數", data["Rating"].mean())
print("中位數", data["Rating"].median())
print("前一百個應用程式的平均", data["Rating"].nlargest(100).mean())
print("前一仟個應用程式的平均", data["Rating"].nlargest(1000).mean())
print("---------------------------------")


data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]",""))
print(data["Installs"])
print("安裝數量", data["Installs"].mean())

condition = data["Installs"]>100000
print("安裝數量大於100000的應用程式有幾個", data[condition].shape[0])
print("---------------------------------")


# 關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字：")
condition=data["App"].str.contains(keyword, case=False)
print(data[condition]["App"])
print(data[condition]["App"].shape[0])