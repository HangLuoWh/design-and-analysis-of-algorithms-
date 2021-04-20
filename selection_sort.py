#给定一个任意长度的数组，将其按照升序排列

def slection_sort(a):
    n = len(a)
    for i in range(n-1):
        min_idx = i # 存储内层循环中当前最小值的索引
        cur_min = a[i] # 存储内层循环种的当前最小值
        for j in range(i+1, n):
            if a[j]<cur_min:
                cur_min = a[j]
                min_idx = j
        temp = a[i]
        a[i] = a[min_idx]
        a[min_idx] = temp

a = [3,2,2,6,8,2,1]
print(a)
print('selection sort:')
slection_sort(a)
print(a)