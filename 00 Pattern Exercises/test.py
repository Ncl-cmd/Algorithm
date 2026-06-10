def dfs_adjacency_list(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    result = [] # Liste pour stocker l'ordre des visites
    # Marquer le nœud actuel comme visité et l'ajouter au résultat
    visited.add(start_node)
    result.append(start_node)

    # Parcourir tous les voisins du nœud actuel
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            # Étendre le résultat avec le parcours du voisin
            result.extend(dfs_adjacency_list(graph, neighbor, visited))

    return result


# --- Test avec l'exemple fourni ---
graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
start = 0

order = dfs_adjacency_list(graph, start)
print(f"Ordre de visite DFS : {order}")
# Sortie attendue : [0, 1, 3, 2]
