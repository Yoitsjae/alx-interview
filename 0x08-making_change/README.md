# Making Change

This project focuses on solving the coin change problem using dynamic programming or greedy algorithms. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. The solution must be both correct and efficient.

## Table of Contents

1. [Project Description](#project-description)
2. [Key Concepts](#key-concepts)
3. [Resources](#resources)
4. [Requirements](#requirements)
5. [Tasks](#tasks)
6. [Setup Instructions](#setup-instructions)
7. [Task Completion](#task-completion)
8. [Additional Notes](#additional-notes)

## Project Description

This project involves solving the coin change problem, which is a classic problem in the domain of dynamic programming and greedy algorithms. The main objective is to determine the minimum number of coins needed to meet a given total amount, using a provided list of coin denominations. The solution must handle scenarios where the total amount cannot be met by the available coins.

## Key Concepts

- Greedy Algorithms: Understanding the principles and limitations of greedy algorithms for solving optimization problems.
- Dynamic Programming: Utilizing dynamic programming techniques to solve the coin change problem efficiently by breaking it down into smaller subproblems.
- Algorithmic Complexity: Analyzing the time and space complexity of algorithms to ensure efficient solutions.
- Problem-Solving Strategies: Employing iterative or recursive approaches to dynamic programming based on problem constraints.
- Python Programming: Implementing efficient looping and conditional statements in Python to manipulate lists and solve algorithmic problems.

## Resources

- Python Official Documentation: [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- GeeksforGeeks Articles: [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/), [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- YouTube Tutorials: [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jgiZlGzXMBw)

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- Files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code must adhere to the PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks

### 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given total amount.

Prototype: `def makeChange(coins, total)`
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list

### Example Usage

```python
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
