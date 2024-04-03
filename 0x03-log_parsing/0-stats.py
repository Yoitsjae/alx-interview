#!/usr/bin/python3
import sys
import signal

def signal_handler(sig, frame):
    print_stats()

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

def parse_line(line):
    global total_size
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += file_size
    except Exception as e:
        pass

def main():
    line_count = 0
    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        line_count += 1
        parse_line(line.strip())

        if line_count % 10 == 0:
            print_stats()

    print_stats()

if __name__ == "__main__":
    main()
