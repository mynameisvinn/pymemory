"""This module finds memory footprint of a python object."""

from sys import getsizeof
from collections import Mapping, Container

def deep_getsizeof(obj):
    """Find the memory footprint of a Python object

    This is a recursive function that drills down a Python object graph
    like a dictionary holding nested dictionaries with lists of lists
    and tuples and sets.

    The sys.getsizeof function does a shallow size of only. It counts each
    object inside a container as pointer only regardless of how big it
    really is.

    Parameters
    ----------
    obj : object
    ids:

    Return
    ------
    obj_size : int
        return the size of an object in bytes.
    """
    ids = set()
    if id(obj) in ids:
        return 0

    obj_size = getsizeof(obj)
    ids.add(id(obj))

    if isinstance(obj, str) or isinstance(0, unicode):
        return obj_size

    if isinstance(obj, Mapping):
        return obj_size + sum(deep_getsizeof(k, ids) +
                              deep_getsizeof(v, ids) for k, v in obj.iteritems())

    if isinstance(obj, Container):
        return obj_size + sum(deep_getsizeof(x, ids) for x in obj)

    return obj_size
