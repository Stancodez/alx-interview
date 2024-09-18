#!/usr/bin/python3
"""
This script defines a function to calculate the minimum number of coins
required to achieve a given total.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    
    Arguments:
    coins -- a list of integers representing coin denominations.
    total -- the total amount we want to achieve using the coins.
    
    Returns:
    The fewest number of coins needed to meet the total.
    If total is 0 or less, returns 0.
    If the total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

