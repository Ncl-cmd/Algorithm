class NumArray:
    def __init__(self, nums: list[int]):
        # Initialize prefix array with a leading 0
        # The size will be len(nums) + 1
        self.prefix = [0] * (len(nums) + 1)

        # Fill the prefix sum array
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, l: int, r: int) -> int:
        # Calculate range sum in O(1) time
        return self.prefix[r + 1] - self.prefix[l]


# Testing the example
nums = [1, 2, 3, 4, 5]
obj = NumArray(nums)

# The prefix array built is: [0, 1, 3, 6, 10, 15]
print(obj.sumRange(1, 3))  # Output: 9
