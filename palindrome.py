def rev_num(n):
    a=0
    while True:
        b=str(n)
        if b==b[::-1]:
            break
        else:
            m=int(b[::-1])
            n+=m
            a+=1
    return n
print(rev_num(1234))      #[1234+4321=5555 ]      
