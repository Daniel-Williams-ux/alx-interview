#!/usr/bin/python3

'''
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped). After every 10 lines and/or a keyboard interruption
(CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print
anything for this status code format: <status code>: <number>
status codes should be printed in ascending order
'''

import re
import sys
from time import sleep
import datetime


counter = 0
file_size = 0
statusC_counter = {200: 0, 301: 0, 400: 0,
                   401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def printCodes(dict, file_s):
    """Prints the status code and the number of times they appear"""
    print("File size: {}".format(file_s))
    for key in sorted(dict.keys()):
        if statusC_counter[key] != 0:
            print("{}: {}".format(key, dict[key]))


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            statusC_and_file_s = split_string[-1]
            if counter != 0 and counter % 10 == 0:
                printCodes(statusC_counter, file_size)
            counter += 1
            try:
                statusC = int(statusC_and_file_s.split()[0])
                f_size = int(statusC_and_file_s.split()[1])
                # print("Status Code {} size {}".format(statusC, f_size))
                if statusC in statusC_counter:
                    statusC_counter[statusC] += 1
                    file_size = file_size + f_size
            except:
                pass
        printCodes(statusC_counter, file_size)
    except KeyboardInterrupt:
        printCodes(statusC_counter, file_size)
        raise
