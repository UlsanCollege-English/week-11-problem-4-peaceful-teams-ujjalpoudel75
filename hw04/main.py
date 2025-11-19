from collections import deque

def bipartition(graph):
    """Return (left_set, right_set) if bipartite; else None.
    BFS-color all components.
    """

    # Nodes include keys + neighbors
    nodes = set(graph)
    for u in graph:
        # Note: 'graph[u]' is the adjacency list, which is iterable
        for v in graph.get(u, []): 
            nodes.add(v)

    color = {}

    # BFS on each uncolored component
    for start in nodes:
        if start in color:
            continue
        color[start] = 0
        q = deque([start])

        while q:
            u = q.popleft()
            # If a node has no adjacency list in graph, treat it as isolated.
            for v in graph.get(u, []):
                if v not in color:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    # Conflict: Found an edge between two nodes of the same color.
                    return None

    # Graph is bipartite. Separate nodes into two sets based on color.
    left = {n for n, c in color.items() if c == 0}
    right = {n for n, c in color.items() if c == 1}
    return (left, right)