from heapq import heappush, heappop

def best_first_search(graph, start, goal, heuristic):
    open_list = []
    closed_list = []
    closed_set = set()
    parent_map = {}
    
    h_start = heuristic(start, goal)
    heappush(open_list, (h_start, start))
    parent_map[start] = None
    
    print("--- Iteration 1 ---")
    print(f"Open List:   [('{start}', None, {h_start})]")
    print(f"Closed List: [()]\n")
    
    step = 1
    
    while open_list:
        h_value, current = heappop(open_list)
        
        print(f"--- Iteration {step + 1}: Selected Node '{current}' ---")
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
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for i in range(num_nodes):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors of {node}: ").split()
        graph[node] = neighbors

    heuristic_values = {}
    for node in graph:
        h_value = int(input(f"Enter heuristic value for {node}: "))
        heuristic_values[node] = h_value
    
    def heuristic(node, goal):
        return heuristic_values.get(node, float('inf'))
    
    start_node = input("Enter the starting node: ")
    goal_node = input("Enter the goal node: ")
    
    path = best_first_search(graph, start_node, goal_node, heuristic)
    
    if path:
        print("\nFinal Path found:", " -> ".join(path))
    else:
        print("\nNo path found.")