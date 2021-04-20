def merge_sort(a):
    n = len(a)
    half = n//2
    if n>1:
        b = a[:half]
        c = a[half:]
        merge_sort(b)
        merge_sort(c)
        merge(b, c, a)

def merge(b, c, a):
    i = 0
    j = 0
    k = 0
    n_b = len(b)
    n_c = len(c)
    while i<n_b and j<n_c:
        if b[i]<c[j]:
            a[k] = b[i]
            i+=1
        else:
            a[k] = c[j]
            j+=1
        k+=1
    if i == n_b:
        a[k:] = c[j:]
    else:
        a[k:] = b[i:]

if __name__ == '__main__':
    a = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98]
    merge_sort(a)
    print(a)