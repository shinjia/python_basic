# 類別的兩種用法
# 1. 類別與類別屬性
# 2. 產生實體物件，實體屬性

# 實體物件：先定義類別，再透過類別建立實體

'''
class 類別名稱:
    # 定義初始化函式
    def __init__(self):
        透過操作 self 來定義體屬性
    # 定義實體方法/函式
    def 方法名稱(self, 更多自訂參數):
        方法主體, 透過 self 操作實體物件

# 建立實體物件，放入變數 obj 中
obj = 類別名稱()  # 呼叫初始化物件
obj.屬性
obj.方法()
'''


# 範例一
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)

p1 = Point(3, 4)
p2 = Point(1, 5)
print(p1.x, p1.y)
print(p2.x, p2.y)

p1.show()
p2.show()



# 範例二
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5

p1 = Point(3, 4)
p2 = Point(1, 5)
result = p1.distance(0, 0)

print(result)