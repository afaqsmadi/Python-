def max_multiple(divisor, bound):
    arr = range(0, bound+1, 1)
    newarr = []
    for num in arr:
        if(num % divisor == 0):
            newarr.append(num)
    else:
        print(newarr[len(newarr)-1])


max_multiple(2, 7)
