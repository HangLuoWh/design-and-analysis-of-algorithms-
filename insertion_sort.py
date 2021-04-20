if __name__ == '__main__':
    a = [3,2,2,6,8,2,1]
    print(a)
    n = len(a)
    for i in range(1, n):
        v = a[i]
        j = i-1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = v
    print('insertion sort:')
    print(a)