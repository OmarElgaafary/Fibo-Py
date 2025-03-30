def fib(max):
    n = 0
    r = n+1
    for i in range(max):
        print(n)
        sum = n+r
        n=r
        r=sum

