# cook your dish here
for t in range(int(input())):
    n,m,k=map(int,input().split())
    arr=list(map(int,input().split()))
    if((arr[n-1] + (k-1)) <= m):
        print("Yes")
    else:
        print("No")