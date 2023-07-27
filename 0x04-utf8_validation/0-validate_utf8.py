#!/usr/bin/python3
"""0-validate_utf8 defines a function validUTF8
"""


def validUTF8(data):
    """checks if a given data set represents a valid
    utf-8 encoding. Reaturns true if data is valid utf-8
    encoding else false
    """
    try:
        byte_data = bytes(data)
        decoded_string = byte_data.decode('utf-8')
        return True
    except (UnicodeDecodeError, ValueError):
        return False
