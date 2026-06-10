def climbStairs(n):
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialization for step 1 and step 2
    first = 1  # ways(1)
    second = 2  # ways(2)

    # Bottom-up calculation up to step n
    for _ in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second


# Testing example
print(climbStairs(1))  # Output: 1
print(climbStairs(5))  # Output: 8