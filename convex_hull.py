import numpy as np
import matplotlib.pyplot as plt

def line(p1, p2, pt):
    a = p2[1]-p1[1]
    b = p1[0]-p2[0]
    c = p1[0]*p2[1]-p1[1]*p2[0]
    if a*pt[0]+b*pt[1]>c:
        return 1
    elif a*pt[0]+b*pt[1]<=c:
        return -1

if __name__ == '__main__':
    points = np.array([[1, 1], [3, 5], [4, 6], [7, 8], [1, 10], [2, 3], [4, 4], [10, 10], [1, 1], [8, 1]])
    plt.figure()
    plt.scatter([i[0] for i in points], [i[1] for i in points])
    n = len(points)
    for i in range(n-1):
        p1 = points[i, :]
        for j in range(i+1, n):
            p2 = points[j, :]
            rest_points = np.delete(points, [i, j], axis=0)
            labels = np.array([line(p1, p2, p) for p in rest_points])
            if (labels==-1).all() or (labels==1).all():
                plt.plot([p1[0], p2[0]], [p1[1], p2[1]], c='r')
    plt.show()