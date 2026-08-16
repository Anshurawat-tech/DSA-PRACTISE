# brute force 
def hcf():
    a=int(input("enter the no."))
    b=int(input("enter the no."))
    c=min(a,b)
    for i in range(c,0,-1):
        if a%i==0 and b%i==0:
            print(i)
            break
        break


# hcf()

# Euclids method
def hcf2():
    a=int(input("enter the greater no:"))
    b=int(input("enter the smaller no:"))
    if a>b:
        a,b=b,a
    else:
        while b>0:
            c=b
            b=a%b
            a=c
            if b==0:
                print("the hcf is :",a)
hcf2()
