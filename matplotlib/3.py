import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r.', t, t*2, 'g,', t, t**2, 'bo')
# plt.plot(t, t, 'rv', t, t*2, 'g^', t, t**2, 'b<', t, t*5, 'c>')
# plt.plot(t, t, 'r1', t, t*2, 'g2', t, t**2, 'b3', t, t*5, 'c4')
# plt.plot(t, t, 'rs', t, t*2, 'gp', t, t**2, 'b*', t, t*5, 'cX')
# plt.plot(t, t, 'rh', t, t*2, 'gH', t, t**2, 'bd', t, t*5, 'cD')
# plt.plot(t, t, 'r+', t, t*2, 'g|', t, t**2, 'b_')
# plt.plot(t, t, 'r-', t, t*2, 'g--', t, t**2, 'b-.', t, t*5, 'c:')

plt.axis([0, 5, 0, 12])
plt.show()