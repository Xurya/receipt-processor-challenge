def alpha_numeric_count(retailer: str) -> int:
    '''Given a string, return the number of alpha numeric characters'''
    count = 0
    for c in retailer:
        if c.isalnum():
            count += 1
    return count

def is_multiple(a, b) -> bool:
    '''Given numbers a and b, determine if a is a multiple of b'''
    if a % b == 0:
        return True
    return False