import random

def randomNumber(min_value: int, max_value: int):
    """"The function takes 2 arguments, both must be 
        given as integers.

        The function returns a random number from 
        the given range."""
    
    value = random.randint(min_value, max_value)

    return value