# Log Parsing

This project involves writing a Python script that reads from standard input (stdin) and computes metrics based on the input data. The input format expected is `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`. The script should handle data in real-time and compute statistics such as total file size and number of lines by status code.

## Usage

To use the script, run it from the command line and pipe the input data into it. For example:

```bash
./0-generator.py | ./0-stats.py
Input Format
The input data should follow the format:

php
Copy code
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Output Format
After every 10 lines of input data and/or a keyboard interruption (CTRL + C), the script prints statistics from the beginning:

Total file size: <total size>
Number of lines by status code:
<status code>: <number>
Status codes considered are: 200, 301, 400, 401, 403, 404, 405, and 500.

Example
yaml
Copy code
./0-generator.py | ./0-stats.py

File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4

Author

This script was written by [Yoitsjae].