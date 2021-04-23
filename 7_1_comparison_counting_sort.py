def ComparisonCountingSort(a):
    n = len(a)
    count = [0]*n # 存储计数的list。
    rlt = [0]*n
    for i in range(n-1):
        cur = a[i]
        for j in range(i+1, n):
            if cur>a[j]: # 此处可以控制是升序还是降序
                count[i]+=1
            else:
                count[j]+=1
    for i in range(n):
        rlt[count[i]] = a[i]
    return rlt

if __name__ == '__main__':
    a = [93, 98, 98, 3, 10, 85, 81, 31]
    print(a)
    b = ComparisonCountingSort(a)
    print(b)