
def doubleLetters(word:str):
    """The function takes 1 argument, type string.
        The function checks if there are two same letters 
        next to ech other in the given string.

        The function returns True if it finds matching letters, 
        or it returns False if neither letter is double.
        """
    
    return any([letter_1 == letter_2 for letter_1, letter_2 in zip(word, word[1:])])

