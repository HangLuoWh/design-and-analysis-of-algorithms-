def lomuto(sub, l, r): # 其中l和r分别表示sub在原始列表中的左右索引值
    key = sub[l] # 为这个key找到一个合适的位置
    i = l # 指向小于key的子列表中最后的一个元素
    j = i+1 # 指向未处理的子列表中的第一个元素
    while j <= r: # 遍历
        if sub[j]<key:
            i+=1 #指针i前进1
            # 调换指针i处和j处的值
            temp = sub[i]
            sub[i] = sub[j]
            sub[j] = temp
        j+=1
    # 调换第一个元素和i的值
    temp = sub[l]
    sub[l] = sub[i]
    sub[i] = temp
    return i

def hoare(sub, l, r):
    key = sub[l]
    i = l+1 # 从左到右检索
    j = r # 从右到左检索
    while i <= j and i<=r:
        if sub[i] >= key and sub[j]<=key:
            temp = sub[i]
            sub[i] = sub[j]
            sub[j] = temp
            i+=1
            j-=1
        else:
            if sub[i]<key:
                i+=1

            if sub[j]>key:
                j-=1
    
    temp = sub[j]
    sub[j] = sub[l]
    sub[l] = temp
    return j
    

def quick_sort(a, l, r):
    if l < r:
        # s = lomuto(a, l, r)
        s = hoare(a, l, r)
        print(f'l:{l}, r:{r}')
        print(a)
        print(a[l:s-1])
        print(a[s+1:r])
        quick_sort(a, l, s-1)
        quick_sort(a, s+1, r)

if __name__ == '__main__':
    a = [93, 98, 14, 3, 27, 85, 81, 31]
    l = 0
    r = len(a)-1
    quick_sort(a, l, r)
    print(a)