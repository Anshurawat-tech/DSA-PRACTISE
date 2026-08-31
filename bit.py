# k th bit is a set or not
def checkbit(n,k):
    if n &( n>>1) >0:
        return True 
    else:
        return False

# Method 2
def checkbit2(n,k):
    if (n>>k) & 1>0:
        return True 
    else:
        return False

print(checkbit2(8,5))   