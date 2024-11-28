#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.
    
    Parameters:
    coins (list): List of coin denominations.
    total (int): Total amount to meet.
    
    Returns:
    int: Minimum number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be made with the given coins
    return dp[total] if dp[total] != float('inf') else -1
