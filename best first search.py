import heapq

def best_first_search(graph, start, goal, heuristic):
    # Priority queue: (heuristic value, node)
    frontier = [(heuristic[start], start)]
    came_from = {start: None}
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)
        visited.add(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in [item[10] for item in frontier]:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'I'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 4,
    'F': 5,
    'G': 3,
    'H': 2,
    'I': 0
}

start_node = 'A'
goal_node = 'I'

path = best_first_search(graph, start_node, goal_node, heuristic)
print("Best First Search path:", path)
