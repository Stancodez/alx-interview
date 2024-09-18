#!/usr/bin/python3

def makeChange(coins, total):
    # If total is 0 or less, we need 0 coins
    if total <= 0:
        return 0
    
    # Initialize an array to store the minimum coins for each amount from 0 to total
    # Set the values to a large number (infinity) initially
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins are needed to make the total 0
    dp[0] = 0
    
    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        # For each coin, check if it can be used to reach the current amount
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If the value at dp[total] is still infinity, the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1

