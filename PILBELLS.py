# cook your dish here
for t in range(int(input())):
    n,x,k,p=map(int,input().split())
    
    if(k<=x):
        level=k*10
    elif(k!=n):
        level=(x*10) + ((k-x)*5) 
    else:
        level = (x*10) + ((k-x)*5) + 20
    print(p+level)
    