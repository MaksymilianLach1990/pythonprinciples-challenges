
def allEqual(items):
    if len(items) == 0:
        return True
    elif len(set(items)) == 1:
        return True
    else:
        return False


def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)