
def countZero(number):
    """The function """
    max_zero = []
    count = 0
    for dige in number:
        if dige == '0':
            count += 1
        else:
            max_zero.append(count)
            count = 0
    
            max_zero.append(count)
    return max(max_zero)



def consecutiveZeros(bin_str):
    return max( [len(s) for s in bin_str.split('1')])