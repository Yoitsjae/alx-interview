#!/usr/bin/python3
"""
Making Change
Author: Jae Ncube
"""

def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to be made with the coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total cannot be met by any number of coins, returns -1.
    """
    # If the total is less than or equal to 0, no coins are needed
    if total <= 0:
        return 0

    # Sort coins in descending order to try the largest denominations first
    coins.sort(reverse=True)
    
    # Temporary variable to keep track of the number of coins used
    coin_count = 0

    # Loop through each coin denomination
    for coin in coins:
        if total >= coin:
            # Use as many of this coin as possible
            coin_count += total // coin
            total %= coin

    # If we have exactly met the total, return the number of coins used
    # Otherwise, return -1 indicating the total cannot be met
    return coin_count if total == 0 else -1

if __name__ == '__main__':
    # Test cases
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
