def powertwo(n):
    c=0
    while n>0:
        if n&1==1:
            c+=1
        n=n//2
    if c==1:
        return True 
    else:
        return False
print(powertwo(8))

# method 2

def powertwo2(n):
    if n!=0 and n&(n-1)==0:
        return True 
    return False
print(powertwo2(10))