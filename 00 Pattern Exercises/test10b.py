def subarraySum(nums: list[int], k: int) -> int:
    count = 0
    current_sum = 0

    # Hash map to store: {prefix_sum : frequency}
    # Base case: a prefix sum of 0 has been seen 1 time (before elements start)
    prefix_sums = {0: 1}

    for num in nums:
        # Update the running prefix sum
        current_sum += num

        # Check if there is a prefix subarray we can subtract to get target k
        if (current_sum - k) in prefix_sums:
            count += prefix_sums[current_sum - k]

        # Record the current prefix sum in the hash map
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

    return count


# Testing the example
print(subarraySum([1, 1, 1], 2))  # Output: 2
