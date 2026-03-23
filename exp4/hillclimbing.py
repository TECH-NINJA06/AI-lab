def hill_climb_search(graph, start, heuristics):
    node = start
    route = [node]
    print("=== START STATE ===")
    print(f"At node: {node} | h={heuristics[node]}\n")
    turn = 1
    while True:
        print(f"=== Turn {turn}: At '{node}' ===")
        neighbors = graph.get(node, [])
        found = None
        for n in neighbors:
            h_n = heuristics[n]
            h_node = heuristics[node]
            print(f"  Inspecting '{n}' [h={h_n}]...", end=" ")
            if h_n < h_node:
                print("Move! (lower h)")
                found = n
                break
            else:
                print("No move.")
        if found is None:
            print("\n⚠️ No lower-h neighbors. Stopping.")
            print(f"Search ends at '{node}' (local/global minimum).")
            break
        node = found
        route.append(node)
        turn += 1
        print(f"\nRoute so far: {' ~ '.join(route)}\n")
    return route

if __name__ == "__main__":
    print("Enter graph nodes (comma separated):")
    nodes = input().strip().split(',')
    nodes = [n.strip() for n in nodes if n.strip()]
    graph = {}
    heuristics = {}
    print("Enter neighbors for each node (comma separated, empty for none):")
    for node in nodes:
        neighbors = input(f"Neighbors of {node}: ").strip()
        graph[node] = [n.strip() for n in neighbors.split(',') if n.strip()]
    print("Enter heuristic value for each node:")
    for node in nodes:
        h_val = input(f"Heuristic for {node}: ").strip()
        try:
            heuristics[node] = float(h_val)
        except ValueError:
            heuristics[node] = float('inf')
    begin = input("Enter start node: ").strip()
    result = hill_climb_search(graph, begin, heuristics)
    print("\n>> Final Route:", " ~ ".join(result))