# 0x0A. Prime Game

## Description

This project involves solving a game where players take turns choosing a prime number from a set of consecutive integers and removing that number and its multiples from the set. The game continues until a player cannot make a move. The goal is to determine the winner of each round based on optimal play.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should follow the PEP 8 style (version 1.7.x)
- All files must be executable

## Files

### `0-prime_game.py`

Contains the implementation of the prime game logic.

#### Prototype

```python
def isWinner(x, nums)
How to Use
Clone the repository or copy the files 0-prime_game.py and main_0.py into your project directory.

Ensure both files have executable permissions.

Run the test script with the following command:

bash
Copy code
./main_0.py
The output will display the winner of the prime game.

Concepts
Prime Numbers
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Sieve of Eratosthenes
An efficient algorithm to find all prime numbers up to a given limit.
Game Theory
The study of mathematical models of strategic interaction among rational decision-makers.
Dynamic Programming / Memoization
Optimization techniques used to improve the efficiency of algorithms by storing previously computed results.
Author: Jae Ncube 