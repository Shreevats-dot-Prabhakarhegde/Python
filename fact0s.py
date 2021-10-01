def ftz(n):
    count=0
    while(n>=5):
        n//=5
        count += n
    return count  
n=100
print("count of trailing 0s" + "in 100! is",ftz(n))