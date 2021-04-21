def pre_sort_bubble(a):
    n = len(a)
    i = 0
    for r in range(n-1):
        i = 0
        while i<=n-2-r:
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
            i+=1

def presort_element_uniqueness(a):
    n = len(a)
    i = 0
    while i <= n-2:
        if a[i] == a[i+1]:
            return False
        i+=1
    return True

if __name__=='__main__':
    a = [93, 98, 98, 3, 10, 85, 81, 31]
    pre_sort_bubble(a) # 预排序
    print(a)
    print(presort_element_uniqueness(a))