def simple_hill_climbing(graph, start, heuristic_values):
    current = start
    path = [current]
    
    print("--- INITIAL STATE ---")
    print(f"Current Node: '{current}' | Heuristic: {heuristic_values[current]}\n")
    
    step = 1
    
    while True:
        print(f"--- STEP {step}: Standing at '{current}' ---")
        neighbors = graph.get(current, [])
        next_node = None
        
        # Evaluate neighbors from left to right
        for neighbor in neighbors:
            h_neighbor = heuristic_values[neighbor]
            h_current = heuristic_values[current]
            
            print(f"  Checking '{neighbor}' (h={h_neighbor})...", end=" ")
            
            # "min to parent" - we want a strictly smaller heuristic
            if h_neighbor < h_current:
                print("Better! Moving here immediately.")
                next_node = neighbor
                break  # We found the first better node, ignore the rest!
            else:
                print("Not better.")
                
        if next_node is None:
            print("\n🛑 No better neighbors found from left to right.")
            print(f"Algorithm terminates. '{current}' is a local/global minimum.")
            break 
            
        current = next_node
        path.append(current)
        step += 1
        print(f"\nPath so far: {' -> '.join(path)}\n")
        
    return path

if __name__ == "__main__":
    # The order in the lists represents left-to-right evaluation
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E'],
        'C': ['F', 'G'],
        'D': ['H'],
        'F': ['I'],
        'G': ['J', 'K']
    }
    
    # We want to minimize these values
    heuristic_values = {
        'A': 10,
        'B': 12, 
        'C': 8,   # Better than A (10)
        'D': 2,   # Much better than A, but we won't reach it because C comes first!
        'E': 14,
        'F': 9,   # Worse than C (8)
        'G': 5,   # Better than C (8)
        'H': 1,
        'I': 10,
        'J': 6,  
        'K': 3    
    }
    
    start_node = 'A'
    
    final_path = simple_hill_climbing(graph, start_node, heuristic_values)
    
    print("\nFinal Hill Climbing Path:", " -> ".join(final_path))