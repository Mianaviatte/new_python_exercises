# Fibonacci No.1 loop way to do it
from linecache import cache


f1 = f2 = 1
n = 22

print ("Fibonacci No.1")
print (f1, end = " ")
print (f2, end = " ")

for i in range(2, n):
    # loop makes next number the sum of previous two
    f1, f2 = f2, f1 + f2
    print (f2, end = " ")

# Fibonacci No.2 Function way to do it
print ("\nFibonacci No.2")

def fib():
    f1,f2 = 0, 1

    while True:
        yield f1
        f1, f2 = f2, f1 + f2

for i, f in zip(range(n+1),fib()):
    print("{i:}:{f:}".format(i = i,f = f))

fib()

# Fibonacci No.3 Recursion way to do it
print ("Fibonacci No.3")

def fibona(n):
    if n==0 : return 0
    if n==1 : return 1

    a = fibona(n-2)
    b = fibona(n-1)
    return a+b;

for i in range(n+1):
    print (fibona(i))

# Fibonacci No.4 Dynamic memorization way to do it
print ("Fibonacci No.4", "ERROR")
cache

def fib_wrap(n):
    cache[n] = [n+1]        #ERROR IS HERE
    return fibonac(n, cache)

def fibonac(n, cache):
    if n==0 : return 0
    if n==1 : return 1

    if cache[n] == 0:
        a = fibonac(n-2, cache)
        b = fibonac(n-1, cache)
        cache[n] = a + b
    return cache[n]

fib_wrap(n)
print (fib_wrap(n))


# Fibonacci No.5 Dynamic tabulation way to do it
print ("Fibonacci No.5", "ERROR")

def fibi(n):
    if n==0 : return 0
    if n==1 : return 1
    
    cache[n] = [n+1]       #ERROR IS HERE
    cache[0] = 0
    cache[1] = 1

    for i in range(2,n):
        cache[i] = cache[i-2] + cache[i-1]
        return cache[n]

print(fibi(n))