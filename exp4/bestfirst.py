
import heapq

def best_first_search(graph, start, goal, heuristic):
    frontier = []
    explored = set()
    parent = {}
    visited_order = []
    closed_list = []
    heapq.heappush(frontier, (heuristic(start, goal), start))
    parent[start] = None
    round_num = 1
    open_nodes = [(start, None, heuristic(start, goal))]
    print(f"=== Iteration {round_num}: Starting at '{start}' ===")
    print(f"Open List: {open_nodes} | Closed List: []\n")
    while frontier:
        h, node = heapq.heappop(frontier)
        print(f"=== Iteration {round_num+1}: Expanding '{node}' (h={h}) ===")
        round_num += 1
        if node == goal:
            print(f"Target '{goal}' found!")
            visited_order.append((node, parent[node], h))
            closed_list.append((node, parent[node], h))
            open_nodes = [(n, parent.get(n), heuristic(n, goal)) for _, n in frontier]
            print(f"Open List: {open_nodes} | Closed List: {closed_list}\n")
            return reconstruct_path(parent, node), visited_order
        if node in explored:
            print(f"'{node}' already explored, skip.\n")
            open_nodes = [(n, parent.get(n), heuristic(n, goal)) for _, n in frontier]
            print(f"Open List: {open_nodes} | Closed List: {closed_list}\n")
            continue
        explored.add(node)
        visited_order.append((node, parent[node], h))
        closed_list.append((node, parent[node], h))
        for neighbor in graph.get(node, []):
            if neighbor not in explored:
                heapq.heappush(frontier, (heuristic(neighbor, goal), neighbor))
                if neighbor not in parent:
                    parent[neighbor] = node
        open_nodes = [(n, parent.get(n), heuristic(n, goal)) for _, n in frontier]
        print(f"Open List: {open_nodes} | Closed List: {closed_list}\n")
    return None, visited_order

def reconstruct_path(parent, node):
    route = []
    while node is not None:
        route.append(node)
        node = parent[node]
    return route[::-1]

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
    def heuristic(n, goal):
        return heuristics.get(n, float('inf'))
    start = input("Enter start node: ").strip()
    end = input("Enter goal node: ").strip()
    result, visited = best_first_search(graph, start, end, heuristic)
    if result:
        print("\n>> Path traced:", " => ".join(result))
    else:
        print("\n>> No path found.")