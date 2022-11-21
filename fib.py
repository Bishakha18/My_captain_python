def febb(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return febb(n-1)+febb(n-2)
    


n=int(input("enter the range of fibnacci series: "))
p=0
for i in range(n):
    p= febb(i)
    print(f"{p}, ",end ="")