#!/usr/bin/python3
"""
Making Change
Author: Jae Ncube

This module solves the coin change problem, determining the fewest number
of coins needed to meet a given total using the provided coin denominations.
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
    # Handle edge cases where total is less than or equal to 0
    if total <= 0:
        return 0

    # Dynamic programming approach to ensure correctness for all cases
    # Create a list to track the minimum coins needed for each amount up to 'total'
    dp = [float('inf')] * (total + 1)  # Initialize with infinity (unreachable state)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Iterate through each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be formed
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == '__main__':
    # Test cases to validate the function
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
