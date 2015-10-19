def flatten_list(list_):
    """ Returnerar en endimensionell lista [a, b, c, d, e],
     givet en tvådimensionell [[a, b], [c], [d, e]]
    """
    return [inner
            for outer in list_
            for inner in outer]

print(flatten_list([[1, 2], [3], [4, 5]]))
