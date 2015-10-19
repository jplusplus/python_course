# -*- coding: utf-8 -*-


def get_unique(list_):
    """Returnerar en lista där varje värde bara förekommer
     en gång.
    """
    return list(set(list_))


def flatten_list(list_):
    """ Returnerar en endimensionell lista [a, b, c, d, e],
     givet en tvådimensionell [[a, b], [c], [d, e]]
    """
    return [inner
            for outer in list_
            for inner in outer]


print(flatten_list([[1, 2], [3], [4, 5]]))

print(get_unique([1, 2, 3, 1, 6, 1, 4, 5]))
