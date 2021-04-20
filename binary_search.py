import math

def binary_search(array, k):
    l = 0
    r = len(array) - 1
    while l<=r:
        m = math.ceil((l+r)/2)
        if array[m] == k: 
            return m
        elif k < array[m]:
            r = m-1
        else:
            l = m+1
    return -1


if __name__ == '__main__':
    a = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98]
    print(a)
    print('biary search:')
    print(binary_search(a, 70))
