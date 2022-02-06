
def addDots(word:str):
    """The function takes 1 argument, type string.
        
        The function returns a string of letters with dots
        added between the letter."""
    return '.'.join(word)

def removeDots(word:str):
    """The function takes 1 argument, type string.
    
        The function removes dots from between letters."""
    return word.replace('.','')