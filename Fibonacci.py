#遞迴
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return f(n - 1) + f(n - 2)

#非遞迴
def fx(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        # 2~n
        temp = b
        b = a + b
        a = temp
    return b

def main():
    n = int(input('第幾項\n'))
    print(fx(n))

if __name__ == '__main__':
    main()