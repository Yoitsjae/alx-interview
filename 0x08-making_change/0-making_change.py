#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array to a large number (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make zero amount

    # Fill dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means it's not possible to make that amount
    return dp[total] if dp[total] != float('inf') else -1

# Example test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
