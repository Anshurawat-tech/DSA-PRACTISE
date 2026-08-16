def lcm():
    a=int(input("enter the no:"))
    b=int(input("enter the no:"))
    c=max(a,b)
    while True:
        if c%a==0 and c%b==0:
            return c
        else:
            c+=max(a.b)
print(lcm())


def lcm2():
    a=int(input("enter the no:"))
    b=int(input("enter the no:"))

    c=(a*b)//hcf(a,b)
    print("lcm of the number is :",c)

lcm2()

