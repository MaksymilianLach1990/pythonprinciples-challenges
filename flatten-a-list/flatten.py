
def flattenList(variable:list):
    """The function takes 1 argument, type list.
        
        The function returns  one list with all 
        the elements in the given argument."""

    return [item for ness in variable for item in ness]