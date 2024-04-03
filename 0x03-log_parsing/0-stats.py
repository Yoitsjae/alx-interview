#!/usr/bin/python3
import sys

class LogParser:
    def __init__(self):
        self.total_file_size = 0
        self.status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
        self.line_count = 0

    def parse_line(self, line):
        parts = line.split()
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = parts[-1]
            if status_code in self.status_codes:
                self.status_codes[status_code] += 1
            try:
                self.total_file_size += int(file_size)
            except ValueError:
                pass

    def print_stats(self):
        print("File size: {}".format(self.total_file_size))
        for code in sorted(self.status_codes.keys()):
            if self.status_codes[code] > 0:
                print("{}: {}".format(code, self.status_codes[code]))

    def process_logs(self):
        try:
            for line in sys.stdin:
                self.line_count += 1
                self.parse_line(line.strip())
                if self.line_count % 10 == 0:
                    self.print_stats()
        except KeyboardInterrupt:
            pass
        self.print_stats()

if __name__ == "__main__":
    parser = LogParser()
    parser.process_logs()
