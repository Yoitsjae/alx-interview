#!/usr/bin/python3
"""
This module implements a script that reads from stdin, parses log data,
and computes statistics based on the input.
"""

import sys
import signal
import re

class LogParser:
    """
    A class to parse log data and compute statistics.
    """

    def __init__(self):
        self.total_size = 0
        self.status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
        self.line_count = 0

    def parse_line(self, line):
        """
        Parses a single log line and updates statistics.
        """
        regex = r"\[(.*?)\] \"GET /projects/260 HTTP/1\.1\" (\d{3}) (\d+)"
        match = re.match(regex, line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            self.total_size += file_size
            if status_code in self.status_codes:
                self.status_codes[status_code] += 1

    def print_stats(self):
        """
        Prints the computed statistics.
        """
        print(f"File size: {self.total_size}")
        for code, count in sorted(self.status_codes.items()):
            if count > 0:
                print(f"{code}: {count}")

    def signal_handler(self, signal, frame):
        """
        Handles keyboard interruption (CTRL + C).
        """
        self.print_stats()
        sys.exit(0)

    def process_logs(self):
        """
        Processes log data from stdin and computes statistics.
        """
        signal.signal(signal.SIGINT, self.signal_handler)
        for line in sys.stdin:
            self.parse_line(line)
            self.line_count += 1
            if self.line_count % 10 == 0:
                self.print_stats()

if __name__ == "__main__":
    parser = LogParser()
    parser.process_logs()
