
def ticTacToeInput(field):
    """The function takes 1 argument, type string.
    
    The function returns a tuple with to numbers
    representing a row and a column."""

    row = "123"
    col = "ABC"

    return row.index(field[1]), col.index(field[0])

