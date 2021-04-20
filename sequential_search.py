# def sequential_search(a, k):
#     n = len(a)
#     a.append(k)
#     idx = 0
#     while a[idx] != k:
#         idx += 1
#     if idx < n:
#         return idx
#     else:
#         return -1

def sequential_search(a, k):
    n = len(a)
    idx = 0
    while idx <=n-1 and a[idx] != k:
        idx+=1
    
    if idx == n:
        return -1
    else:
        return idx

a = [3,2,2,6,8,2,1]
print(a)
print('sequential search:')
print(sequential_search(a, 10))