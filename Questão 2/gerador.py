import sys
import random
import numpy as np

size = int(5000)

out_file_x = open('data_x.txt', 'w')
out_file_y = open('data_y.txt', 'w')

out_data = []

for _ in range(size):
    x = random.random() * 4
    y = np.sin(np.pi * x) / (np.pi * x)

    out_data.append([x, y])

random.shuffle(out_data)

for data in out_data:
    out_file_x.write(str(data[0])+'\n')
    out_file_y.write(str(data[1])+'\n')