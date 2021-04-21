if __name__ == '__main__':
    c =[3, 4, -2, -5]
    x = 2
    value = c[0]
    print(value)
    for i in range(1, len(c)):
        value = value*x + c[i]
        print(value)