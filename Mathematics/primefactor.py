def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def primefactor(n):
    for i in range(2,n+1):
        if isprime(i):
            x=i
            while n%x==0:
                print(i)
                x=x*i
primefactor(16)