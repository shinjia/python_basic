# 開啟檔案
# 檔案物件 = open(檔案路徑, mode=開啟模式)
# 開啟模式 (r, w, r+)

# 寫入文字到檔案內
# 檔案物件.write(文字)

# 關閉檔案
# 檔案物件.close()

# 最佳實務 (會自動、安全的關閉檔)
# with open(檔案路徑, mode=讀寫模式) as 檔案物件：
#   讀取或寫入檔案的程式


filename = "temp.txt"
# file = open(filename, mode="w", encoding="utf-8")
# file.write("Hello File")
# file.write("Line 1\nLine 2\n")
# file.write("中文字")
# file.close()

with open(filename, mode="w", encoding="utf-8") as file:
    file.write("測試中文\nHello World")

with open(filename, mode="r", encoding="utf-8") as file:
    data = file.read()
print(data)


# 讀取檔案裡各列的數字並計算總和
with open(filename, mode="w", encoding="utf-8") as file:
    file.write("5\n3\n7\n8")

sum = 0
with open(filename, mode="r", encoding="utf-8") as file:
    for line in file:  # 逐列讀取
        sum += int(line)
print(sum)
