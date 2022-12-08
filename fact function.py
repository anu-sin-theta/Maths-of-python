def factsum(*a):
    def fact(b):
        if(b==0):
            return 1
        else:
            f=1
            for m in range(1,b+1):
                f*=m
            return f
    s = 0
    for i in a:
        if i >=0:
            s+=fact(i)
    return s
print(factsum(1,2,3,4,5,0))



