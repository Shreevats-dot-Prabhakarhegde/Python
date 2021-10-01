def fibonacci(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)
for f in range (12): # by putting any no here
    print (fibonacci(f))                