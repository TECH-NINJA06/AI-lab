def simple_hill_climbing(graph, start, heuristic_values):
    current = start
    path = [current]
    
    print("--- INITIAL STATE ---")
    print(f"Current Node: '{current}' | Heuristic: {heuristic_values[current]}\n")
    
    step = 1
    
    while True:
        print(f"--- STEP {step}: Node '{current}' ---")
        neighbors = graph.get(current, [])
        next_node = None
        
        for neighbor in neighbors:
            h_neighbor = heuristic_values[neighbor]
            h_current = heuristic_values[current]
            
            print(f"  Checking '{neighbor}' (h={h_neighbor})...", end=" ")
            
            if h_neighbor < h_current:
                print("Better")
                next_node = neighbor
                break  
            else:
                print("Not better.")
                
        if next_node is None:
            print("\nNo better neighbors found from left to right.")
            print(f"Algorithm terminates. '{current}' is a local minimum.")
            break 
            
        current = next_node
        path.append(current)
        step += 1
        print(f"\nPath: {' -> '.join(path)}\n")
        
    return path

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
    
    start_node = input("Enter the starting node: ")
    
    final_path = simple_hill_climbing(graph, start_node, heuristic_values)
    
    print("\nFinal Hill Climbing Path:", " -> ".join(final_path))