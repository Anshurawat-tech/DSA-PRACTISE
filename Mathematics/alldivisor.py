def divisor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)

def divisor2(n):
    i=1
    l=[]
    m=[]

    while (i*i<=n):
        if n%i==0:
            l.append(i)
            if i!=n/i:
                m.append(n/i)

        i+=1
    return l[:]+m[::-1]
print(divisor2(16))
