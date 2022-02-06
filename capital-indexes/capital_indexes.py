
def capitalIndexes(text: str):
    """The function takes 1 argument in the form of a string.
        The function checks the position of uppercase letters.

        The function returns a list of indexes."""
    return [number for number in range(len(text)) if text[number] == text[number].upper()]

