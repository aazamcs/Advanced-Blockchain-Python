""" This python file contains blockchain tools. """

from hashlib import sha256


def calculate_hash(*args) -> str:
    """ Takes in *args and produce a sha256 hash. """
    hashing_text = ''
    h = sha256()

    # hash each argument
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()
