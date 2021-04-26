import numpy as np

def coin_collection(c):
    f = np.zeros_like(c)
    f[0, 0] = c[0, 0]
    h, w = c.shape
    for i in range(1, w):
        f[0, i] = f[0, i-1] + c[0, i]
    for i in range(1, h):
        f[i, 0] = f[i-1, 0] + c[i, 0]
        for j in range(1, w):
            f[i, j] = max(f[i-1, j], f[i, j-1])+c[i, j]
    print(f)

if __name__ == '__main__':
    c = np.zeros((5, 6))
    c[0, 4] = 1
    c[1, 1] = 1
    c[1, 3] = 1
    c[2, 3] = 1
    c[2, 5] = 1
    c[3, 2] = 1
    c[3, 5] = 1
    c[4, 0] = 1
    c[4, 4] = 1
    print(c)
    coin_collection(c)