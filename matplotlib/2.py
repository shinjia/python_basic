import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.plot([2020, 2021, 2022, 2023], [1, 4, 9, 16])

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.plot([1, 2, 3, 4], [4, 5, 7, 6], 'g^')
plt.axis([0, 6, 0, 20])  # 指定 x, y 軸的尺標


plt.show()
