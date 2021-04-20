def lomuto_partition(a):
    p = a[0]
    s = 0 # 记录小于第一个数的部分的最大索引
    for i in range(1, len(a)):
        if a[i] < p:
            s += 1
            temp = a[s]
            a[s] = a[i]
            a[i] = temp
    temp = a[0]
    a[0] = a[s]
    a[s] = temp

if __name__=='__main__':
    a=[50, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98]

    print(a)
    print('lomuto partition:')
    lomuto_partition(a)
    print(a)