
def onlineStatus(people:dict):
    """The function takes 1 argument, a dictionary.
        The function checks the status of each user in the dictionary.
        
        The function returns the number of users with the 'online' status."""
    
    return list(people.values()).count("online")
