def numIslands(grid):
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
        dfs(r + 1, c)  # Bas
        dfs(r - 1, c)  # Haut
        dfs(r, c + 1)  # Droite
        dfs(r, c - 1)  # Gauche
    # Traverse each cell of the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)  # Trigger the DFS to sink/mark the entire island
    return count


# Example
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(numIslands(grid))  # Sortie : 1
