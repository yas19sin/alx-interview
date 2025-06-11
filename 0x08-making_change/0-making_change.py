#!/usr/bin/python3
"""
Making Change - Dynamic Programming Solution
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin values available
        total (int): Target amount to make change for

    Returns:
        int: Fewest number of coins needed to meet total,
             0 if total is 0 or less,
             -1 if total cannot be met
    """
    if total <= 0:
        return 0

    # Initialize dp array where dp[i] represents minimum coins for amount i
    # Use total + 1 as "infinity" since we can't use more than total coins
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Fill the dp array using dynamic programming
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still total + 1, it means total cannot be made
    return dp[total] if dp[total] != total + 1 else -1
