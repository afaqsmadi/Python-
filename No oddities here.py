# Return list of only even values
def no_odds(values):
    arr = []
    for val in values:
        if val % 2 == 0:
            arr.append(val)
    else:
        print(arr)


no_odds([-1, -3, -5, -7, -9])
