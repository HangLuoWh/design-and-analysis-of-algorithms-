def coin_row(a):
    n = len(a)
    if n == 0:
        return 0
    elif n == 1:
        return a[0]
    elif n == 2:
        return max(*a)
    else:
        return max(a[0] + coin_row(a[2:]), coin_row(a[1:]))
if __name__ == '__main__':
    coins = [5, 1, 2, 10, 6, 2]
    print(coin_row(coins))