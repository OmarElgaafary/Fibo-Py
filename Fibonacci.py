def fib(max):
    n, r = 0, 1
    for i in range(max):
        print(n)
        sum = n+r
        n=r
        r=sum


fib(30)