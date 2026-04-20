from heapq import heappush, heappop

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def manhattan_distance(state):
    dist = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_idx = tile - 1
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_idx, 3)
        dist += abs(x1 - x2) + abs(y1 - y2)
    return dist


def get_neighbors(state):
    neighbors = []
    z = state.index(0)
    r, c = divmod(z, 3)

    moves = []
    if r > 0:
        moves.append(-3)  # up
    if r < 2:
        moves.append(3)   # down
    if c > 0:
        moves.append(-1)  # left
    if c < 2:
        moves.append(1)   # right

    for m in moves:
        nz = z + m
        lst = list(state)
        lst[z], lst[nz] = lst[nz], lst[z]
        neighbors.append(tuple(lst))

    return neighbors


def is_solvable(state):
    """8-puzzle solvability check using inversion count."""
    arr = [x for x in state if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2 == 0


def reconstruct_path(parent, end_state):
    path = []
    cur = end_state
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]


def print_state(state):
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


def a_star(start, show_local_minima=False):
    if start == GOAL:
        return [start]
    if not is_solvable(start):
        return None

    open_heap = []
    g_cost = {start: 0}
    parent = {start: None}

    heappush(open_heap, (manhattan_distance(start), 0, start))
    visited = set()

    while open_heap:
        f, g, state = heappop(open_heap)

        if state in visited:
            continue
        visited.add(state)

        if state == GOAL:
            return reconstruct_path(parent, state)

        neighbors = get_neighbors(state)

        if show_local_minima:
            h_cur = manhattan_distance(state)
            h_neighbors = [manhattan_distance(n) for n in neighbors]
            if all(hn >= h_cur for hn in h_neighbors):
                print(f"Local minima hit at g={g}, h={h_cur}, f={f}:")
                print_state(state)

        for nxt in neighbors:
            tentative_g = g + 1
            if nxt not in g_cost or tentative_g < g_cost[nxt]:
                g_cost[nxt] = tentative_g
                parent[nxt] = state
                h = manhattan_distance(nxt)
                heappush(open_heap, (tentative_g + h, tentative_g, nxt))

    return None


if __name__ == "__main__":
    print("Sequence of states from start to goal:\n")
    start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    inp = input("Enter the start state as 9 values (0 for blank), separated by spaces: ").strip()
    start_state = tuple(int(x) for x in inp.split())
    if len(start_state) != 9 or set(start_state) != set(range(9)):
        raise ValueError("Invalid input. Enter each number from 0 to 8 exactly once.")

    path = a_star(start_state, show_local_minima=True)

    if path is None:
        print("No solution exists for this start state.")
    else:
        print(f"Solved in {len(path) - 1} moves.\n")
        for step, s in enumerate(path):
            print(f"Step {step}:")
            print_state(s)