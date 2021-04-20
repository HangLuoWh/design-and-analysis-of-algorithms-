# 冒泡排序

def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

a = [3,2,2,6,8,2,1]
print(a)
print('selection sort:')
bubble_sort(a)
print(a)