#!/usr/bin/python3
"""
This module implements a script that generates random log data
in the specified format.
"""

import random
import sys
from time import sleep
import datetime

def generate_log():
    """
    Generates a random log line.
    """
    ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    current_time = datetime.datetime.now()
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)
    return f"{ip_address} - [{current_time}] \"GET /projects/260 HTTP/1.1\" {status_code} {file_size}"

if __name__ == "__main__":
    for _ in range(10000):
        sleep(random.random())
        sys.stdout.write(f"{generate_log()}\n")
        sys.stdout.flush()
