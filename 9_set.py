# SET 集合 (一群資料，沒有順序性)
# - 判斷資料是否存在 (in, not in)
# - 交集、聯集 (& |)
# - 差集、反交集 (- ^)
# - 字串拆解為集合 (set(字串))

# ------------------------------------------------

# 判斷資料是否存在 (in, not in)
s1 = { 5, 7, 3 }
print( 2 in s1)
print( 3 in s1)
print( 3 not in s1)

# 交集、聯集 (& |)
s1 = { 5, 7, 3}
s2 = { 3, 4, 5}
s3 = s1 & s2  # 交集
s4 = s1 | s2  # 聯集
print(s3)
print(s4)

# 差集、反交集 (- ^)
s1 = { 5, 7, 3}
s2 = { 3, 4}
s3 = s1 - s2
s4 = s1 ^ s2
print(s3)
print(s4)

# 字串拆解為集合 (set(字串))
s = set("Hello World")
print(s)
print(" " in s)

ss ="Hello World"  # 字串也可以使用 in
print(" " in ss)
