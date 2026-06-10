from collections import deque
from contextlib import redirect_stderr


def bfs_adjacency_list(graph, start_node):
    # Initialize the queue with the start node
    queue = deque([start_node])
    visited = {start_node}
    result=[]

graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
start = 0  # -> [0, 1, 2, 3]
bfs_adjacency_list(graph, start)