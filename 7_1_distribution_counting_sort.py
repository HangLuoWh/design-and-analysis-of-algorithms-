def DistributionCountingSort(a, l, u):
    n = len(a)
    count = [0]*(u-l+1)
    rlt = [0]*n
    for i in a:
        count[i-l]+=1
    for j in range(1, u-l+1):
        count[j] = count[j]+count[j-1]
    for i in range(n):
        rlt[count[a[i]-l]-1] = a[i]
        count[a[i]-l] -= 1
    return rlt

if __name__ == '__main__':
    a = [12, 12, 13, 11, 14, 13, 13]
    b = DistributionCountingSort(a, 11, 14)
    print(b)