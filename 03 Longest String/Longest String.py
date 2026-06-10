class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        Find the longest palindromic substring in s.
        Time Complexity: O(n²) - where n is the length of the string.
        Spatial Complexity: O(1) - the algorithm uses constant memory.
        """
        if not s or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            # Case 1: The palindrome has an odd center (e.g., "aba", center = 'b')
            len1 = self._expand_around_center(s, i, i)
            # Case 2: The palindrome has an even center (e.g., "abba", center = between 'b' and 'b')
            len2 = self._expand_around_center(s, i, i + 1)
            # We keep the maximum length found
            max_len = max(len1, len2)
            # If a palindrome longer than the previous one is found, the indices are updated.
            if max_len > (end - start):
                # Clever calculation to find the beginning and end from the center i
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]

    def _expand_around_center(self, s: str, left: int, right: int) -> int:
        """A helpful method for extending a palindrome and reversing its length."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Returns the length of the palindrome found
        return right - left - 1

if __name__ == "__main__":
    s = Solution()

    str = "abcabcbb"
    result = s.longestPalindrome(str)
    print(f"Result : {result}")  # Should display "bab"

    str = "bbbbb"
    result = s.longestPalindrome(str)
    print(f"Result : {result}")  # Should display "bbbbb"

    str = "cbbd"
    result = s.longestPalindrome(str)
    print(f"Result : {result}")  # Should display "bb"

    str = "abcadef"
    result = s.longestPalindrome(str)
    print(f"Result : {result}")  # Should display "f"

    str = "abba"
    result = s.longestPalindrome(str)
    print(f"Result : {result}")  # Should display "abba"
