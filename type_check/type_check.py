
def onlyInts(value_1, value_2):
    """The function takes 2 arguments any type.
        The function checks the type of given values.
        
        The function returns True if both values are integer,
        if one of the values is of a diffrent type it returns False. """

    if type(value_1) == int and type(value_2) == int:
        return True
    else:
        return False
