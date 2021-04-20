import matplotlib.pyplot as plt

def dis(a, b):
    rlt = 0
    for i in range(len(a)):
        rlt += (a[i]-b[i])**2
    return rlt**(1/2)

if __name__ =='__main__':
    points = [[1, 1], [3, 5], [4, 6], [7, 8], [1, 10], [2, 3]]
    plt.figure()
    plt.scatter([i[0] for i in points], [i[1] for i in points])
    n= len(points)
    min_len = None
    min_i = -1
    min_j = -1
    for i in range(n-1):
        for j in range(i+1, n):
            distance = dis(points[i], points[j])
            if min_len == None or min_len > distance:
                min_len = distance
                min_i = i
                min_j = j
    min_points = [points[min_i], points[min_j]]

    plt.scatter([i[0] for i in min_points], [i[1] for i in min_points], c='r')
    plt.show()