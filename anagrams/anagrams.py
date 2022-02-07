
def isAnagram(word_1, word_2):
    """The function takes 2 argument, both type string.
        
        The function returnes True if the same letters are
        present in both values."""
    return sorted(word_1) == sorted(word_2)
