# 字典
# - key-value Pair
# - key 對應 value 
# - 判斷資料是否存在 (in, not in)
# - 刪除鍵值對 (del)
# - 從串列建立字典

# ------------------------------------------------

# s1 = { "apple", "banana" }
# s2 = { "蘋果","香蕉" }

# key-value Pair (key 對應 value)
dic = {"apple":"蘋果", "banana":""}
dic["banana"] = "香蕉"
print(dic)
print(dic["apple"])

# 判斷資料是否存在 (in, not in)，判斷 key
print("apple")

# 刪除鍵值對 (del)
del dic["apple"]
print(dic)

# 從串列建立字典
dic = {x:x*2 for x in [2, 3, 4]}
print(dic)
