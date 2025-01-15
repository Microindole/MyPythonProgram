count=0
s=0
def f(n):
    global s;global count
    for i in range(1,3):
        if i==1 and n>1:
            s+=1
            f(n-1)
        elif i==2 and n>1:
            s+=2
            f(n-1)
    return count
            

            
