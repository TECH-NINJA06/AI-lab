def is_valid_state(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def solve_missionaries_and_cannibals_dfs():
    initial_state = (3, 3, 1) 
    goal_state = (0, 0, 0)
    
    stack = [(initial_state, [initial_state], [])]
    visited = set([initial_state])
    
    boat_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while stack:
        (m, c, b), states, actions = stack.pop() 

        if (m, c, b) == goal_state:
            print("--- SOLUTION FOUND (DFS) ---")
            print("Format: (Missionaries on Left, Cannibals on Left, Boat Position)")
            
            start_b = 'L' if states[0][2] == 1 else 'R'
            print(f"Start : ({states[0][0]}, {states[0][1]}, {start_b})")
            
            for i in range(len(actions)):
                left_m, left_c, boat_pos = states[i+1]
                b_str = 'L' if boat_pos == 1 else 'R'
                print(f"Step {i+1}: {actions[i].ljust(22)} -> State: ({left_m}, {left_c}, {b_str})")
            
            print(f"\nTotal steps: {len(actions)}")
            return

        for dm, dc in boat_moves:
            if b == 1:
                next_state = (m - dm, c - dc, 0)
                action_str = f"Move {dm}M, {dc}C Right"
            else:
                next_state = (m + dm, c + dc, 1)
                action_str = f"Move {dm}M, {dc}C Left"

            if is_valid_state(next_state[0], next_state[1]) and next_state not in visited:
                visited.add(next_state)
                stack.append((next_state, states + [next_state], actions + [action_str]))

    print("No solution found.")

solve_missionaries_and_cannibals_dfs()