class Solution(object):
    def longest_string(self, str) -> int:
        """
        :type str: string
        """
        """
        Calculates the length of the longest substring without repeated characters.
        Time Complexity: O(n) - a single traversal of the string.
        Space Complexity: O(min(m, n)) - size of the dictionary to store the characters.
        """
        # Dict used to store the last index seen of each char
        window = {}
        max_length = 0
        start = 0  # Début de la fenêtre glissante
        # print(str)
        for end, char in enumerate(str):
            # If the character is already in the current window, the beginning of the window is moved.
            if char in window and window[char] >= start:
                start = window[char] + 1
            # We update or add the position of the current character
            window[char] = end
            # We calculate the size of the current window and keep the maximum value
            max_length = max(max_length, end - start + 1)
            # print(window, start, max_length)
        return max_length

if __name__ == "__main__":
    s = Solution()

    str = "abcabcbb"
    result = s.longest_string(str)
    print(f"Result : {result}")  # Should display 3

    str = "bbbbb"
    result = s.longest_string(str)
    print(f"Result : {result}")  # Should display 1

    str = "pwwkew"
    result = s.longest_string(str)
    print(f"Result : {result}")  # Should display 3

    str = "aA1!aA1!"
    result = s.longest_string(str)
    print(f"Result : {result}")  # Should display 4

    str = "abcadef"
    result = s.longest_string(str)
    print(f"Result : {result}")  # Should display 6

    str = "abba"
    result = s.longest_string(str)
    print(f"Result : {result}")  # Should display 2
