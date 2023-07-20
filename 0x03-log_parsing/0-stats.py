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
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET /projects/\d+ HTTP/1\.1" \d+ \d+$'
    try:
        for line in sys.stdin:
            if bool(re.match(pattern, line)):
                if count > 0 and count % 10 == 0:
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
                        status_codes = {key: value + 1 if key == code else value for key, value in status_codes.items()}
                count = count + 1
            else:
                continue
    except KeyboardInterrupt:
        print('File size: {}'.format(size))
        for key, value in status_codes.items():
            if value > 0:
                print("{}: {}".format(key, value))
        raise


if __name__ == "__main__":
    main()
