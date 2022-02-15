
def tripleAnd(item1, item2, item3):
    """The function takes 3 arguments.
    
        The function returns True if all values are True,
        otherwise returns False."""
        
    return all(item == True for item in (item1, item2, item3))

def triple_and(a, b, c):
    """The function takes 3 arguments.
    
        The function returns True if all values are True,
        otherwise returns False."""

    return a and b and c