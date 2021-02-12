# 迴圈句型 while (沒有 do--while語法)
# while 布林值:
n = 1
while n<5:
    print("變數 n 的資料是 ", n)
    n += 1

# 迴圈 for
# for 變數名稱 in 串列或字串:
for x in [5, 2, 3, 6]:
    print(x)

for x in "Hello":
    print(x)

for x in range(3):  # 相當於 [0, 1, 2]
    print(x)

for x in range(3, 6):  # 相當於 [3, 4, 5]
    print(x)


# 迴圈搭配的命令 break, continue