def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)

def lcm(m, n):
    greatest = gcd(m, n)
    return int(m*n/greatest)

if __name__ == '__main__':
    print(lcm(3, 4))