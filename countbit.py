def countbit(n):
    res=0
    while n:
        if (n%2==1):
            res+=1
        n=n//2
    return res
print(countbit(40))


# method 2 
def countbit2(n):
    res=0
    while n :
        n=n&(n-1)
        res=res+1
    return res
print(countbit2(40))