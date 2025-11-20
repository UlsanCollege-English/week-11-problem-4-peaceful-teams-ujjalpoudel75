"""
HW04 — Peaceful Teams (Bipartite Check)

Implement:
- bipartition(graph)
"""

from collections import deque

def bipartition(graph):
    """Return (left_set, right_set) if the graph is bipartite; else None.

    The graph is an adjacency-list dict representing an undirected graph.
    Use BFS coloring over all components:
    - Maintain a color dict: node -> 0 or 1
    - For each uncolored node, start BFS, color it 0
    - Neighbors get the opposite color
    - If a conflict is found (same-color neighbors), return None
    """
    color = {}  # node -> 0 or 1

    for start in graph:
        if start not in color:
            color[start] = 0
            queue = deque([start])

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    else:
                        # Same-colored neighbor → not bipartite
                        if color[v] == color[u]:
                            return None

    # Build the two teams (sets)
    left = {node for node, c in color.items() if c == 0}
    right = {node for node, c in color.items() if c == 1}

    return (left, right)
