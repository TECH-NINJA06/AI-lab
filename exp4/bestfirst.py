from heapq import heappush, heappop

def best_first_search(graph, start, goal, heuristic):
    open_list = []
    closed_list = []
    closed_set = set()
    parent_map = {}
    
    h_start = heuristic(start, goal)
    heappush(open_list, (h_start, start))
    parent_map[start] = None
    
    print("--- INITIAL STATE (Before Loop) ---")
    print(f"Open List:   [('{start}', None, {h_start})]")
    print(f"Closed List: []\n")
    
    step = 1
    
    while open_list:
        h_value, current = heappop(open_list)
        
        print(f"--- STEP {step}: Selected Node '{current}' ---")
        step += 1
        
        if current == goal:
            print(f"Goal '{goal}' reached!")
            closed_list.append((current, parent_map[current], h_value))
            path = reconstruct_path(parent_map, current)
            return path
        
        if current in closed_set:
            print("Node already evaluated, skipping.\n")
            continue
        
        closed_set.add(current)
        closed_list.append((current, parent_map[current], h_value))
        
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in closed_set:
                    h_neighbor = heuristic(neighbor, goal)
                    heappush(open_list, (h_neighbor, neighbor))
                    if neighbor not in parent_map:
                        parent_map[neighbor] = current
        
        open_formatted = [(node, parent_map.get(node), h) for h, node in open_list]
        closed_formatted = [(node, parent, h) for node, parent, h in closed_list]
        
        print(f"Open List:   {open_formatted}")
        print(f"Closed List: {closed_formatted}\n")
    
    return None

def reconstruct_path(parent_map, node):
    path = []
    current = node
    while current is not None:
        path.append(current)
        current = parent_map[current]
    return path[::-1]

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    heuristic_values = {
        'A': 3, 'B': 2, 'C': 4, 'D': 0, 'E': 1, 'F': 0
    }
    
    def heuristic(node, goal):
        return heuristic_values.get(node, float('inf'))
    
    start_node = 'A'
    goal_node = 'F'
    
    path = best_first_search(graph, start_node, goal_node, heuristic)
    
    if path:
        print("\nFinal Path found:", " -> ".join(path))
    else:
        print("\nNo path found.")