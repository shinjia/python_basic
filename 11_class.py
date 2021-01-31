# 封裝變數或函式

# 定義類別
# class 類別名稱
#   定義封裝變數
#   定義封裝函式

# 使用類別
# - 類別名稱.屬性名稱 

class Test:
    x = 3
    def show():
        print("Hello")

print(Test.x * 2)
print(Test.show())


# 範列
class IO:
    supportedSrcs = ["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Read from", src)

print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")