
N = 4

cols = list(range(N))

def is_safe_swap(cols, col):
	for c in range(col):
		if cols[c] == cols[col] or abs(cols[c] - cols[col]) == abs(c - col):
			return False
	return True

def solve(col):
	if col >= N:
		return True

	for i in range(col, N):
		cols[col], cols[i] = cols[i], cols[col]

		if is_safe_swap(cols, col):
			if solve(col + 1):
				return True

		cols[col], cols[i] = cols[i], cols[col]

	return False

def print_solution():
	for r in range(N):
		for c in range(N):
			if cols[c] == r:
				print("Q", end=" ")
			else:
				print(".", end=" ")
		print()

if solve(0):
	print("Solution Found:\n")
	print_solution()
else:
	print("No Solution Exists")

