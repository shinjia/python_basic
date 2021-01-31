# 讀取 JSON 格式
# import json
# - 讀取到的資料 = json.load(檔案物件)
# 讀取 JSON
# - json.load(檔案物件)
# 寫入 JSON 
# - json.dump(要寫入的資料, 檔案物件)
'''
{
    "name": "Shinjia",
    "version": "1.2.1"
}
'''

import json
with open("data.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

print(data)  # 讀入的格式為 Dictionary
print("name:", data["name"])
print("version:", data["version"])

data["name"] = "Allen"
data["version"] = "1.2.4"

with open("data.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file)