def change_make(d, n):
    f = [0]*(n+1)
    n_d = len(d)
    for i in range(1, n+1):
        temp = 100000
        j = 0
        while j <= n_d-1 and i - d[j] >= 0:
            temp = min(f[i-d[j]], temp)
            j+=1
        f[i] = temp+1
    return f[n-1]

if __name__ == '__main__':
    d = [1, 3, 4]
    n = 6
    print(change_make(d, n))