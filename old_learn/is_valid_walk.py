def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    north = walk.count('n')
    south = walk.count('s')
    east = walk.count('e')
    west = walk.count('w')

    return north == south and east == west