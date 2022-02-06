
def middleLetter(string):
    """The function takes 1 argument as a string.
        The function checks which letter is in the middle.
        
        The function returns a specific letter if the number of letter is odd,
        if number of letter is even it returns an empty string."""
    
    if len(string) % 2 != 0:
        return string[len(string)//2]
    else:
        return ""

