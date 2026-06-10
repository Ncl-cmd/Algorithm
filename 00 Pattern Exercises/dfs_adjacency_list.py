def dfs_adjacency_list(graph, start_node):
    visited = set()
    result = []
    def dfs(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Explore all neighbors of the current node
            for neighbor in graph[node]:
                dfs(neighbor)
    dfs(start_node)
    return result

# Exemple fourni
graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
print(dfs_adjacency_list(graph, 0))
