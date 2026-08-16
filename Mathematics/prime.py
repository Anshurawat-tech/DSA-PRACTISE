def prime(n):
    i=2
    if n<=1:
        return False
    
    elif i*i<n:
        if n%i==0:
            return False
        i+=1
    return True
print(prime(2))
    