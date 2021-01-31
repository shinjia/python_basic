class File:
    # 初始化方法
    def __init__(self, name):
        self.name = name
        self.file = None  ## 尚未開啟檔案，初期是 None
    # 實體方法
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()

# 讀取第一個檔案
f1 = File("data1.txt")
f1.open()
data = f1.read()
print(data)

f2 = File("data2.txt")
f2.open()
data = f2.read()
print(data)