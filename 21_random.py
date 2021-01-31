# 隨機亂數模組
# 統計模組

import random
data = [0, 1, 2, 3, 4, 5, 6]
print(random.choice(data))
print(random.sample(data, 2))

data = [2, 4, 6, 2]
random.shuffle(data)
print(data)

print(random.random())  # 取得 0~1(不含) 的隨機亂數
print(random.uniform(0.0, 1.0))
print(random.normalvariate(100, 10))  # 常態分配，參數是平均數和標準差
print("-------------------------------")


import statistics
data = [2, 4, 6, 8, 9]
statistics.mean(data)
statistics.median(data)
statistics.stdev(data)