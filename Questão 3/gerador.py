import numpy as np
import matplotlib.pyplot as plt

data = np.array([p for p in 2*np.random.rand(10000, 2) -
                 1 if np.linalg.norm(p) < 1])
data.shape

def labelPoint(p):
    c = [p[0] > 0, p[1] > 0, np.sum(np.abs(p)) > 1]
    return sum([int(c[i])*2**i for i in range(3)])

y = [labelPoint(p) for p in data]
print(len(y))
colors = {0: 'black', 1: 'red', 2: 'blue', 3: 'green',
          4: 'orange', 5: 'purple', 6: 'hotpink', 7: 'yellow'}

plt.figure(figsize=(5, 5))
plt.scatter(data[:, 0], data[:, 1], s=3, c=[colors[yp] for yp in y])
plt.axis('equal')
plt.show()

np.savetxt('data_x.txt', data, delimiter=',')
np.savetxt('data_y.txt',
           np.array(y).astype(np.int), fmt='%d', delimiter=',')