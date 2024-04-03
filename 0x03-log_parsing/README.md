# 0x03. Log Parsing

## Project Description
This project involves writing a Python script that reads from standard input (stdin) line by line, parses log entries, and computes metrics based on the input data. The script is expected to handle data in a specific format and perform calculations to generate statistics.

### Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Code should follow the PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks
### 0. Log Parsing
Write a script that reads stdin line by line and computes metrics based on the input log data.

- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> 
- Print statistics after every 10 lines and/or keyboard interruption (CTRL + C)
  - Total file size
  - Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)

Author

This script was written by [Yoitsjae].