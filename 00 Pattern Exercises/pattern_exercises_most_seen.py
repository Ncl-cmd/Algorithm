# =============================================================================
# ALGORITHMIC PATTERNS — EXERCISES
# 10 core patterns, 2 exercises each (warm-up + interview-style)
# =============================================================================
# HOW TO USE
# ----------
# Each exercise has:
#   - A docstring explaining the problem and examples
#   - A function stub to complete
#   - A run_tests() call at the bottom to check your answers
#
# Run the full file:   python pattern_exercises.py
# Run one section:     comment out the run_tests() calls you don't want
# =============================================================================


# =============================================================================
# PATTERN 1 — TWO POINTERS
# =============================================================================

def two_pointers_warmup(s: str) -> bool:
    """
    WARM-UP — Check if a string is a palindrome.

    A palindrome reads the same forwards and backwards.
    Use two pointers starting at each end and moving inward.
    Do NOT use slicing (s == s[::-1]) — the point is to practice the pattern.

    Examples:
        "racecar"  -> True
        "hello"    -> False
        "a"        -> True
        ""         -> True
    """
    j = len(s) - 1
    k = []
    if j <= 0:
        return True
    for i in range(j // 2 + 1):
        # print(f"{s[i]}  ---  {s[j-i]}")
        if s[i] == s[j - i]:
            k.append(True)
        else:
            k.append(False)
    # print(k)
    return not (False in k)


def two_pointers_interview(nums: list[int], target: int) -> list[int]:
    """
    INTERVIEW — Two sum in a sorted array.

    Given a sorted array of integers and a target, return the indices [i, j]
    (1-indexed) of the two numbers that add up to the target.
    Exactly one solution is guaranteed. You may not use the same element twice.

    Constraint: O(n) time, O(1) space — no hash map allowed.

    Examples:
        [2, 7, 11, 15], target=9   -> [1, 2]
        [1, 4, 6, 8],   target=10  -> [2, 3]
        [-3, 0, 4, 8],  target=5   -> [1, 4]
    """
    k = len(nums)
    # print(f"The target sum is {target} on the input string: {nums}, whose length is {k}")
    for i in range(k):  # range outputs 0...(k-1)           if k=4, range 0,1,2,3
        for j in range(k - 1, i, -1):  # range will start at k down to i   if i=1, range 3,2,1
            # print(f"i:{i}  j:{j}  ",end="")
            # print(f"i+j:{nums[i]+nums[j]}")
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]
    return []


# =============================================================================
# PATTERN 2 — SLIDING WINDOW
# =============================================================================

def sliding_window_warmup(nums: list[int], k: int) -> int:
    """
    WARM-UP — Maximum sum of k consecutive elements.

    Given an array of integers and a window size k, return the maximum
    sum of any contiguous subarray of length k.

    Compute the first window, then slide: subtract the element leaving,
    add the element entering. No nested loops.

    Examples:
        [2, 1, 5, 1, 3, 2],  k=3  -> 9   (subarray [5, 1, 3])
        [1, 4, 2, 9],        k=2  -> 11  (subarray [2, 9])
        [5],                 k=1  -> 5
    """
    j = len(nums)
    # print(f"The max sum of a {k} digit window taken from the input string: {nums} is:")
    max_sum = 0
    for i in range(j - k // 2):
        s = sum(nums[i:i + k])
        # print(f"i:{i}  i+k:{i+k}  sum:{s}")
        if s > max_sum:
            max_sum = s
    return max_sum


def sliding_window_interview(s: str) -> int:
    """
    INTERVIEW — Longest substring without repeating characters.

    Given a string, return the length of the longest substring that contains
    no duplicate characters. Use a variable-size sliding window: expand right,
    shrink left when a duplicate enters the window.

    Examples:
        "abcabcbb"  -> 3   ("abc")
        "bbbbb"     -> 1   ("b")
        "pwwkew"    -> 3   ("wke")
        ""          -> 0
    """
    k = len(s)
    max_s = 0
    x = set()
    for i in range(k):
        x.add(s[i])
        for j in range(i + 1, k - 1):
            if s[j] not in x:
                x.add(s[j])
            else:
                max_s = max(max_s, len(x))
                x = set()
            # print(f"i:{i}  j:{j}  x:{x}")
    return max_s


# =============================================================================
# PATTERN 3 — BINARY SEARCH
# =============================================================================

def binary_search_warmup(nums: list[int], target: int) -> int:
    """
    WARM-UP — Classic binary search.

    Given a sorted array and a target, return the index of the target.
    Return -1 if not found. Implement from scratch — no bisect module.

    Examples:
        [1, 3, 5, 7, 9], target=5  -> 2
        [1, 3, 5, 7, 9], target=6  -> -1
        [1],             target=1  -> 0

    Do NOT use this easy but SLOW and not binary method !
        k = len(nums)
        for i in range(k):
            if nums[i] == target:
                    return i
        return -1
    """
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_interview(nums: list[int], target: int) -> int:
    """
    INTERVIEW — Search in a rotated sorted array.

    A sorted array was rotated at some unknown pivot (e.g. [4,5,6,7,0,1,2]).
    Given this rotated array and a target, return its index or -1.
    Must run in O(log n).

    Key insight: one half of the array is always sorted after a rotation.
    Determine which half is sorted, then decide which half to search.

    Examples:
        [4, 5, 6, 7, 0, 1, 2], target=0  -> 4
        [4, 5, 6, 7, 0, 1, 2], target=3  -> -1
        [1],                   target=0  -> -1
        [3, 1],                target=1  -> 1
    """
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:  # Target found
            return mid
        if nums[low] <= nums[mid]:  # Condition 1: The left half is perfectly sorted
            if nums[low] <= target < nums[mid]:  # Check if the target is located in this sorted left area
                high = mid - 1  # Look to the left
            else:
                low = mid + 1  # Look to the right
        else:  # Condition 2 : The right half is perfectly sorted
            if nums[mid] < target <= nums[high]:  # Check if the target is located in this sorted right area
                low = mid + 1  # Look to the right
            else:
                high = mid - 1  # Look to the left
    return -1


# =============================================================================
# PATTERN 4 — RECURSION & BACKTRACKING
# =============================================================================

def backtracking_warmup(n: int) -> list[list[int]]:
    """
    WARM-UP — Generate all subsets of [1, 2, ..., n].

    Return every possible subset (the power set), including the empty set.
    Order of subsets does not matter.

    Template to follow:
        def backtrack(start, current):
            add a copy of current to results
            for i in range(start, n+1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

    Examples:
        n=2  -> [[], [1], [1, 2], [2]]          (any order)
        n=3  -> [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
    """
    results = []

    def backtrack(start, current):
        results.append(list(current))  # We add a copy of the current subset
        for i in range(start, n + 1):  # We traverse the integers from 'start' up to and including 'n'
            current.append(i)
            backtrack(i + 1, current)  # Exploration with the next integer
            current.pop()  # Coming back (Backtrack)

    backtrack(1, [])
    return results


def backtracking_interview(nums: list[int]) -> list[list[int]]:
    """
    INTERVIEW — All permutations of a list of unique integers.

    Return all possible orderings of the input list.
    Classic interview question — expected O(n * n!) time.

    Examples:
        [1, 2, 3]  -> [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        [0, 1]     -> [[0,1], [1,0]]
        [1]        -> [[1]]
    """
    results = []
    n = len(nums)
    used = [False] * n  # Allows you to track items already selected

    def backtrack(current):
        if len(current) == n:  # If the current permutation is complete, we add it
            results.append(list(current))
            return
        for i in range(n):  # We try each element of the list for the current position
            if not used[i]:  # Choice
                used[i] = True
                current.append(nums[i])
                backtrack(current)  # Exploration
                current.pop()  # Coming back (Backtrack)
                used[i] = False

    backtrack([])
    return results


# =============================================================================
# PATTERN 5 — HASH MAP / HASH SET
# =============================================================================

def hashmap_warmup(values: list[int], target: int) -> list[int]:
    """
    WARM-UP — Two sum (unsorted).

    Given an unsorted array and a target, return the indices [i, j] of the
    two numbers that add up to target. Each input has exactly one solution.

    Use a hash map: for each number, check if (target - number) is already
    stored. If yes, you found the pair.

    Examples:
        [2, 7, 11, 15], target=9   -> [0, 1]
        [3, 2, 4],      target=6   -> [1, 2]
        [3, 3],         target=6   -> [0, 1]
    """
    seen = {}  # Dictionary to store: {value: index}
    for i, num in enumerate(values):  # ❌✅ enumerate ✅❌
        complement = target - num  # Calculate the required complement to reach the target
        if complement in seen:  # If the complement is already in the dictionary, we found the pair
            return [seen[complement], i]
        seen[num] = i  # Otherwise, save the current number and its index


def hashmap_interview(str_list: list[str]) -> list[list[str]]:
    """
    INTERVIEW — Group anagrams.

    Given a list of strings, group the anagrams together.
    An anagram uses the same letters in a different order ("eat", "tea", "ate").

    Approach: use a sorted version of each word as the hash map key.
    All words that are anagrams share the same sorted key.

    Examples:
        ["eat","tea","tan","ate","nat","bat"]
            -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]  (any order)
        [""]      -> [[""]]
        ["a"]     -> [["a"]]
    """
    anagram_map = {}
    for word in str_list:  # ❌✅ "".join() ✅❌
        sorted_key = "".join(sorted(word))  # Sort the characters to create the signature key
        if sorted_key not in anagram_map:  # Initialize the list if the key is seen for the first time
            anagram_map[sorted_key] = []  # ❌✅ Append ✅❌
        anagram_map[sorted_key].append(word)  # Append the original word to its anagram group
    return list(anagram_map.values())  # Return all the grouped lists


# =============================================================================
# PATTERN 6 — DEPTH-FIRST SEARCH (DFS)
# =============================================================================

def dfs_warmup(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    WARM-UP — DFS traversal order on an adjacency list.

    Given a graph as an adjacency list and a start node, return the list of
    nodes visited in DFS order (visit each node before its neighbors).
    Use a visited set to avoid revisiting.

    Example graph: {0: [1, 2], 1: [3], 2: [3], 3: []}

        0 -> 1 -> 3
        0 -> 2 -> 3  (already visited)

    Examples:
        graph={0:[1,2], 1:[3], 2:[3], 3:[]}, start=0  -> [0, 1, 3, 2]
    """
    visited = set()
    result = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Explore all neighbors of the current node
            for neighbor in graph[node]:
                dfs(neighbor)

    dfs(start)
    return result


def dfs_interview(grid: list[list[str]]) -> int:
    """
    INTERVIEW — Number of islands.

    Given a 2D grid of '1' (land) and '0' (water), count the number of islands.
    An island is a group of '1's connected horizontally or vertically.

    Approach: iterate the grid. When you find a '1', increment the counter
    and run DFS to mark all connected land cells as visited ('0' or '#').

    Examples:
        [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]]  -> 1

        [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]  -> 3
    """

    if not grid:
        return 0
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):
        # Check the grid boundaries and whether the cell is '1'.
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        # Mark the cell as visited by transforming it into water '0'
        grid[r][c] = '0'
        # Visit the 4 orthogonal neighbors (up, down, left, right)
        dfs(r + 1, c)  # Low
        dfs(r - 1, c)  # High
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    # Traverse each cell of the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)  # Trigger the DFS to sink/mark the entire island
    return count


# =============================================================================
# PATTERN 7 — BREADTH-FIRST SEARCH (BFS)
# =============================================================================

def bfs_warmup(graph: dict[int, list[int]], start: int) -> list[int]:
    """
    WARM-UP — BFS traversal order on an adjacency list.

    Given the same graph as the DFS warm-up, return nodes in BFS order
    (visit all neighbors at distance 1, then distance 2, etc.).
    Use a queue (collections.deque) and a visited set.

    Examples:
        graph={0:[1,2], 1:[3], 2:[3], 3:[]}, start=0  -> [0, 1, 2, 3]
    """
    from collections import deque

    def bfs_adjacency_list(graph, start_node):
        # Initialize the queue with the start node
        queue = deque([start_node])
        # Track visited nodes to avoid infinite loops
        visited = {start_node}
        result = []
        while queue:
            # Remove and return the front element of the queue
            current_node = queue.popleft()
            result.append(current_node)

            # Check all neighbors of the current node
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)              # ❌✅ queue.append ✅❌
        return result


def bfs_interview(grid: list[list[int]]) -> int:
    """
    INTERVIEW — Shortest path in a binary maze.

    Given an n x n grid of 0s and 1s, return the length of the shortest
    clear path from the top-left (0,0) to the bottom-right (n-1, n-1).
    A clear cell has value 0. You can move in 8 directions.
    Return -1 if no path exists.

    BFS guarantees the shortest path in an unweighted grid.
    Path length = number of cells visited (including start and end).

    Examples:
        [[0,1],[1,0]]   -> 2
        [[0,0,0],[1,1,0],[1,1,0]]  -> 4
        [[1,0,0],[1,1,0],[1,1,0]]  -> -1  (start blocked)
    """
    from collections import deque

    def shortestPathBinaryMatrix(grid):
        n = len(grid)

        # Edge Case: If the start or end cell is blocked, no path exists
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # Queue stores tuples of (row, col, path_length)
        queue = deque([(0, 0, 1)])

        # In-place tracking: mark visited cells as 1 to avoid a separate set
        grid[0][0] = 1

        # Define all 8 possible movements (horizontal, vertical, and diagonal)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        while queue:
            r, c, length = queue.popleft()

            # If we reached the bottom-right corner, return the path length
            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries and ensure the neighbor cell is clear (0)
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1  # Mark as visited
                    queue.append((nr, nc, length + 1))

        return -1


# =============================================================================
# PATTERN 8 — DYNAMIC PROGRAMMING
# =============================================================================

def dp_warmup(n: int) -> int:
    """
    WARM-UP — Climbing stairs.

    You can climb 1 or 2 steps at a time. How many distinct ways are there
    to reach the top of a staircase with n steps?

    This is Fibonacci in disguise:
        ways(1) = 1
        ways(2) = 2
        ways(n) = ways(n-1) + ways(n-2)

    Use a bottom-up table or two variables — no recursion.

    Examples:
        n=1  -> 1
        n=2  -> 2
        n=3  -> 3
        n=5  -> 8
    """
    # Base cases
    if n <= 0:
        return 0
    if n <= 2:
        return n
    # Initialization for step 1 and step 2
    first = 1  # ways(1)
    second = 2  # ways(2)

    # Bottom-up calculation up to step n
    for _ in range(3, n + 1):
        current = first + second
        first = second
        second = current

    return second


def dp_interview(amount: int, coins: list[int]) -> int:
    """
    INTERVIEW — Coin change (minimum coins).

    Given a list of coin denominations and a target amount, return the minimum
    number of coins needed to make up that amount.
    Return -1 if it's impossible.

    Build a dp table where dp[i] = min coins to make amount i.
    Initialize dp[0] = 0 and dp[1..amount] = infinity.
    For each amount i, try every coin: dp[i] = min(dp[i], dp[i - coin] + 1).

    Examples:
        amount=11, coins=[1,2,5]   -> 3   (5+5+1)
        amount=3,  coins=[2]       -> -1
        amount=0,  coins=[1]       -> 0
    """
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


# =============================================================================
# PATTERN 9 — STACK
# =============================================================================

def stack_warmup(s: str) -> bool:
    """
    WARM-UP — Valid parentheses.

    Given a string of brackets, return True if it is valid.
    Valid means: every opening bracket has a matching closing bracket
    in the correct order.

    Brackets: '()', '[]', '{}'

    Examples:
        "()"       -> True
        "()[]{}"   -> True
        "(]"       -> False
        "([)]"     -> False
        "{[]}"     -> True
    """

    # Hash map to instantly look up corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        # If the character is a closing bracket
        if char in mapping:
            # Pop the top element from stack if not empty, else use a dummy value
            top_element = stack.pop() if stack else '#'

            # The popped opening bracket must match the required one
            if mapping[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return len(stack) == 0


def stack_interview(temperatures: list[int]) -> list[int]:
    """
    INTERVIEW — Daily temperatures (next warmer day).

    Given a list of daily temperatures, return a list where answer[i] is
    the number of days you have to wait after day i to get a warmer temperature.
    If no warmer day exists, answer[i] = 0.

    Use a stack of indices of days with unresolved temperatures.
    When a warmer day arrives, pop and resolve all colder days on the stack.

    Examples:
        [73,74,75,71,69,72,76,73]  -> [1,1,4,2,1,1,0,0]
        [30,40,50,60]              -> [1,1,1,0]
        [30,60,90]                 -> [1,1,0]
    """

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


# =============================================================================
# PATTERN 10 — PREFIX SUMS
# =============================================================================

def prefix_warmup(nums: list[int], l: int, r: int) -> int:
    """
    WARM-UP — Range sum query.

    Given an array, precompute prefix sums so you can answer range queries
    in O(1). Return the sum of elements from index l to r (inclusive).

    prefix[0] = 0
    prefix[i] = prefix[i-1] + nums[i-1]
    sum(l, r) = prefix[r+1] - prefix[l]

    Examples:
        nums=[1,2,3,4,5], l=1, r=3  -> 9  (2+3+4)
        nums=[1,2,3,4,5], l=0, r=4  -> 15
        nums=[3,7,2],     l=0, r=0  -> 3
    """

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


def prefix_interview(nums: list[int], k: int) -> int:
    """
    INTERVIEW — Subarray sum equals k.

    Given an array of integers and a value k, return the total number of
    contiguous subarrays whose sum equals k.

    Brute force is O(n²). Optimal approach uses prefix sums + a hash map:
    - Track running prefix sum
    - At each index, check if (prefix_sum - k) has been seen before
    - If yes, there are that many subarrays ending here with sum k

    Examples:
        [1, 1, 1], k=2   -> 2
        [1, 2, 3], k=3   -> 2   (subarrays [1,2] and [3])
        [1,-1,1],  k=1   -> 3
    """

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


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    results = []

    def check(name, got, expected):
        if isinstance(expected, list) and expected and isinstance(expected[0], list):
            passed = sorted(map(tuple, got)) == sorted(map(tuple, expected))
        else:
            passed = got == expected
        status = "PASS" if passed else "FAIL"
        results.append((status, name, got, expected))

    # --- Two pointers ---
    check("two_pointers_warmup: racecar", two_pointers_warmup("racecar"), True)
    check("two_pointers_warmup: hello", two_pointers_warmup("hello"), False)
    check("two_pointers_warmup: empty", two_pointers_warmup(""), True)
    check("two_pointers_interview: [2,7,11,15] t=9", two_pointers_interview([2, 7, 11, 15], 9), [1, 2])
    check("two_pointers_interview: [1, 4, 6, 8] t=10", two_pointers_interview([1, 4, 6, 8], 10), [2, 3])
    check("two_pointers_interview: [-3, 0, 4, 8] t=5", two_pointers_interview([-3, 0, 4, 8], 5), [1, 4])

    # --- Sliding window ---
    check("sliding_window_warmup: k=3", sliding_window_warmup([2, 1, 5, 1, 3, 2], 3), 9)
    check("sliding_window_warmup: k=2", sliding_window_warmup([1, 4, 2, 9], 2), 11)
    check("sliding_window_interview: abcabcbb", sliding_window_interview("abcabcbb"), 3)
    check("sliding_window_interview: bbbbb", sliding_window_interview("bbbbb"), 1)
    check("sliding_window_interview: pwwkew", sliding_window_interview("pwwkew"), 3)

    # --- Binary search ---
    check("binary_search_warmup: found", binary_search_warmup([1, 3, 5, 7, 9], 5), 2)
    check("binary_search_warmup: missing", binary_search_warmup([1, 3, 5, 7, 9], 6), -1)
    check("binary_search_interview: rotated hit", binary_search_interview([4, 5, 6, 7, 0, 1, 2], 0), 4)
    check("binary_search_interview: rotated miss", binary_search_interview([4, 5, 6, 7, 0, 1, 2], 3), -1)
    check("binary_search_interview: [3,1] t=1", binary_search_interview([3, 1], 1), 1)

    # --- Backtracking ---
    check("backtracking_warmup: n=2", backtracking_warmup(2), [[], [1], [1, 2], [2]])
    check("backtracking_interview: [1,2,3]", backtracking_interview([1, 2, 3]),
          [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

    # --- Hash map ---
    check("hashmap_warmup: [2,7,11,15]", hashmap_warmup([2, 7, 11, 15], 9), [0, 1])
    check("hashmap_warmup: [3,2,4]", hashmap_warmup([3, 2, 4], 6), [1, 2])
    check("hashmap_interview: anagrams",
          hashmap_interview(["eat", "tea", "tan", "ate", "nat", "bat"]),
          [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    # --- DFS ---
    # g = {0:[1,2], 1:[3], 2:[3], 3:[]}
    # check("dfs_warmup",       dfs_warmup(g, 0), [0,1,3,2])
    # check("dfs_interview: 1 island",
    #       dfs_interview([["1","1","1","1","0"],["1","1","0","1","0"],
    #                      ["1","1","0","0","0"],["0","0","0","0","0"]]), 1)
    # check("dfs_interview: 3 islands",
    #       dfs_interview([["1","1","0","0","0"],["1","1","0","0","0"],
    #                      ["0","0","1","0","0"],["0","0","0","1","1"]]), 3)

    # --- BFS ---
    # check("bfs_warmup",       bfs_warmup(g, 0), [0,1,2,3])
    # check("bfs_interview: path=2",  bfs_interview([[0,1],[1,0]]),              2)
    # check("bfs_interview: path=4",  bfs_interview([[0,0,0],[1,1,0],[1,1,0]]), 4)
    # check("bfs_interview: no path", bfs_interview([[1,0,0],[1,1,0],[1,1,0]]), -1)

    # --- DP ---
    # check("dp_warmup: n=1",  dp_warmup(1), 1)
    # check("dp_warmup: n=5",  dp_warmup(5), 8)
    # check("dp_interview: 11 coins=[1,2,5]", dp_interview(11, [1,2,5]), 3)
    # check("dp_interview: 3  coins=[2]",     dp_interview(3,  [2]),     -1)
    # check("dp_interview: 0  coins=[1]",     dp_interview(0,  [1]),     0)

    # --- Stack ---
    # check("stack_warmup: ()",      stack_warmup("()"),     True)
    # check("stack_warmup: (]",      stack_warmup("(]"),     False)
    # check("stack_warmup: {[]}",    stack_warmup("{[]}"),   True)
    # check("stack_interview: temps", stack_interview([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])
    # check("stack_interview: asc",   stack_interview([30,40,50,60]),             [1,1,1,0])

    # --- Prefix sums ---
    # check("prefix_warmup: l=1 r=3", prefix_warmup([1,2,3,4,5], 1, 3), 9)
    # check("prefix_warmup: l=0 r=4", prefix_warmup([1,2,3,4,5], 0, 4), 15)
    # check("prefix_interview: k=2",  prefix_interview([1,1,1], 2), 2)
    # check("prefix_interview: k=3",  prefix_interview([1,2,3], 3), 2)

    # --- Print summary ---
    passed = sum(1 for r in results if r[0] == "PASS")
    total = len(results)
    print(f"\n{'=' * 60}")
    print(f"  Results: {passed}/{total} passed")
    print(f"{'=' * 60}")
    for status, name, got, expected in results:
        if status == "FAIL":
            print(f"  FAIL  {name}")
            print(f"        got:      {got}")
            print(f"        expected: {expected}")
    if passed == total:
        print("  All tests passed!")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    run_tests()
