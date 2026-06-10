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
                queue.append(neighbor)
    return result

# Example provided
graph={0:[1,2], 1:[3], 2:[3], 3:[]}
start=0
print(bfs_adjacency_list(graph, start))  # Output: [0, 1, 2, 3]
