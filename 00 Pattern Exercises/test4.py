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


# Example provided
grid = [[0, 1],
        [1, 0]]
print(shortestPathBinaryMatrix(grid))  # Output: 2
