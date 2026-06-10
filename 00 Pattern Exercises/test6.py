def coinChange(coins, amount):
    # Initialize the DP table with a value representing infinity
    # amount + 1 is safe because you can never need more than 'amount' coins (using 1-cent coins)
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 coins are needed to make an amount of 0
    dp[0] = 0

    # Compute the minimum coins for every sub-amount from 1 to 'amount'
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the target amount remains infinity, it means it is impossible to make
    return dp[amount] if dp[amount] != float('inf') else -1


# Testing the example
print(coinChange([1, 2, 5], 11))  # Output: 3
