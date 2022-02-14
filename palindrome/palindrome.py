
def palindrome(word:str):
    """The function takes 1 argument, type string.
    
        The function returns True if the string is
        a palindrome, otherwise it returns False. """
    
    if word == word[::-1]:
        return True
    else:
        return False