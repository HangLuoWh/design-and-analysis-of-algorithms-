def insert_sort(a):
    n = len(a)
    for i in range(1, n):
        v = a[i]
        j = i-1
        while a[j] >= v and j >= 0:
            a[j+1] = a[j] # 将排好序的子数组向后平移
            j-=1
        a[j+1] = v

def presort_mode(a):
    n = len(a)
    mode_value = None
    mode_fre = 0
    i = 0
    while i <= n-1:
        run_length = 1
        cur_value = a[i]
        while i+run_length <= n-1 and a[i+run_length] == cur_value:
            run_length += 1
        if run_length > mode_fre:
            mode_fre = run_length
            mode_value = cur_value
        i += run_length
    return mode_value, mode_fre

if __name__ == '__main__':
    a = [93, 98, 98, 31, 10, 85, 98, 81, 85,31]
    insert_sort(a)
    print(a)
    print(presort_mode(a))