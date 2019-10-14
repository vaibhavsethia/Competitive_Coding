for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=sorted(list(map(int,input().split())),reverse=True)
    if n==1:
        print(1)
    elif k==n:
        print(n)
    else:    
        m=arr[k-1]
        if arr[k]<m:
            print(k)
        else:
            d=arr[k:]
            f=d.count(arr[k-1])
            print(f+k)
        
    
