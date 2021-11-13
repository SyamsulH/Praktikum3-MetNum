# Interpolasi Lagrange

import numpy as np

# Membaca jumlah titik data
n = int(input('masukan jumlah titik data: '))

# Membuat array ukuran n x n dan inisiasi
x = np.zeros((n))
y = np.zeros((n))

# Membaca titik data
print('masukan data x dan y: ')
for i in  range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))

# Membaca interpolasi titik
xp = float(input('masukan x yang diinginkan: '))

# Inisiasi interpolasi
yp = 0

# Implementasi interpolasi Lagrange
for i in range (n):

    p = 1

    for j in range (n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])

    yp = yp + p * y[i]

# Displaying  output
print('nilai interpolasi untuk %.3f adalah %.3f.' % (xp, yp))