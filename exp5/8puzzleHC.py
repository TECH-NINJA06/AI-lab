GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def print_board(state):
	for i in range(0, 9, 3):
		print(" ".join("_" if x == 0 else str(x) for x in state[i : i + 3]))
	print()


def read_state(prompt):
	while True:
		raw = input(prompt).strip().replace('"', "").replace("'", "")
		parts = raw.split()
		if len(parts) != 9:
			print("Please enter exactly 9 numbers separated by spaces.")
			continue
		try:
			state = tuple(int(x) for x in parts)
		except ValueError:
			print("Only integers are allowed.")
			continue
		if set(state) != set(range(9)):
			print("Numbers must contain each value from 0 to 8 exactly once.")
			continue
		return state


def inversions(state):
	a = [x for x in state if x != 0]
	return sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j])


def is_solvable(start, goal):
	return inversions(start) % 2 == inversions(goal) % 2


def manhattan(state, goal_pos):
	d = 0
	for i, tile in enumerate(state):
		if tile:
			r, c = divmod(i, 3)
			gr, gc = goal_pos[tile]
			d += abs(r - gr) + abs(c - gc)
	return d


def neighbors(state):
	z = state.index(0)
	zr, zc = divmod(z, 3)
	out = []
	for dr, dc in MOVES:
		nr, nc = zr + dr, zc + dc
		if 0 <= nr < 3 and 0 <= nc < 3:
			s = list(state)
			n = nr * 3 + nc
			s[z], s[n] = s[n], s[z]
			out.append(tuple(s))
	return out


def hill_climb(start, goal):
	goal_pos = {tile: divmod(i, 3) for i, tile in enumerate(goal)}
	current = start
	path = [current]
	visited = {current}

	while True:
		if current == goal:
			return path, True
		cur_h = manhattan(current, goal_pos)
		cands = [s for s in neighbors(current) if s not in visited]
		if not cands:
			return path, False
		scored = [(manhattan(s, goal_pos), s) for s in cands]
		best_h = min(h for h, _ in scored)
		best = sorted(s for h, s in scored if h == best_h)[0]
		if best_h >= cur_h:
			return path, False
		current = best
		visited.add(current)
		path.append(current)


def main():
	print("8-Puzzle Solver (Hill Climbing - Steepest Ascent)")
	print("Use 0 for the blank tile.")
	print()

	start = read_state("Enter START state (9 numbers, space-separated): ")
	if not is_solvable(start, GOAL):
		print("\nThis start and goal pair is unsolvable (inversion parity mismatch).")
		return

	path, solved = hill_climb(start, GOAL)

	print("\nStart state:")
	print_board(start)
	print("Goal state:")
	print_board(GOAL)
	print("Path explored by hill climbing:\n")
	for step, state in enumerate(path):
		print(f"Step {step}:")
		print_board(state)

	if not solved:
		print(f"Hill climbing got stuck in a local optimum after {len(path) - 1} moves.")
		print("Try a different start state or use A* for guaranteed path search.")
		return

	print(f"Solved in {len(path) - 1} moves.")


if __name__ == "__main__":
	main()
