def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Stores indices of days

    for current_day in range(n):
        current_temp = temperatures[current_day]

        # Resolve indices in the stack if the current day is warmer
        while stack and temperatures[stack[-1]] < current_temp:
            prev_day = stack.pop()
            answer[prev_day] = current_day - prev_day

        # Push the current day's index onto the stack
        stack.append(current_day)

    return answer


# Testing the example
temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temps))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
