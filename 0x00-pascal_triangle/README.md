# Pascal's Triangle

This Python project generates Pascal's triangle up to a given number of rows and displays it.



1. Clone the repository:

```bash
git clone https://github.com/your_username/pascals-triangle.git
Navigate to the project directory:
bash
Copy code
cd pascals-triangle
Run the main script:
bash
Copy code
python3 pascal_triangle.py
Example
python
Copy code
from pascal_triangle import pascal_triangle

triangle = pascal_triangle(5)
for row in triangle:
    print(row)
Output
csharp
Copy code
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
Files
pascal_triangle.py: Contains the implementation of the pascal_triangle function.
0-main.py: Main script to demonstrate the functionality of the pascal_triangle function.