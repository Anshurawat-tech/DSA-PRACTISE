def power(x,n):
    if n==0:
        return 1
    temp=power(x,n//2)
    temp=temp*temp
    if(n%2==0): 
        return temp
    else:
        return temp*x

# another method 

def power2(x,n):
    res=1
    while n>0:
        if n%2!=0:
            res=res*x
        x=x*x
        n=n//2
    return res
print(power2(2,4))