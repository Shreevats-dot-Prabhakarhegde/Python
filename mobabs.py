def abs_digits(n):
    all_nums = set([0,1,2,3,4,5,6,7,8,9])
    n=set([int(i) for i in n])
    n=n.symmetric_difference(all_nums)
    n=sorted(n)
    return n
print(abs_digits([1,2,3,3,1,4,5,8,9,0]))