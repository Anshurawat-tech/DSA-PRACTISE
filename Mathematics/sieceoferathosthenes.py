# sieve of eratosthenes
def sieve():
    n=int(input("enter the mo."))
    prime=[True]*(n+1)
    prime[0]=False
    prime[1]=False
    i=2
    while i*i<=n:
        if prime[i]==True:
            for j in range(i*i,n+1,i):
                prime[j]=False
        i+=1
    res=[]
    for i in range(2,n+1):
        if prime[i]==True:
            res.append(i)
    return res
print(sieve())
