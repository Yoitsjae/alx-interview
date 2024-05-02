#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given total amount
"""

def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed for each total from 0 to total
    min_coins = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total of 0
    min_coins[0] = 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update min_coins list for each total
        for i in range(coin, total + 1):
            # Calculate the minimum number of coins needed for current total
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # If the value at index total is still infinity, total cannot be met
    return min_coins[total] if min_coins[total] != float('inf') else -1

# Example usage
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
