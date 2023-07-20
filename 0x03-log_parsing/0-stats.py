#!/usr/bin/python3
"""0-stats defines a function main that reads stdin
line by line and computes metrics
"""
import sys
import re
from time import sleep


def main():
    """reads stdin line by line and computes metrics
    """
    status_codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
    }
    size = 0
    count = 0
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    pattern = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    try:
        for line in sys.stdin:
            if bool(re.match(pattern, line)):
                if count % 10 == 0 and count > 0:
                    count = 0
                    print('File size: {}'.format(size))
                    for key, value in status_codes.items():
                        if value > 0:
                            print("{}: {}".format(key, value))
                else:
                    lst = line.strip().split(' ')
                    file = int(lst[-1])
                    size = size + file
                    code = int(lst[-2])
                    if type(code) is int:
                        if code in status_codes.keys():
                            status_codes[code] += 1
                    count = count + 1
            else:
                continue
    except (KeyboardInterrupt, EOFError):
        print('File size: {}'.format(size))
        for key, value in status_codes.items():
            if value > 0:
                print("{}: {}".format(key, value))
        raise


if __name__ == "__main__":
    main()
