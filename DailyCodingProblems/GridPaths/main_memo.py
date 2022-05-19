def create_random_large_grid(rows: int = 1000, cols: int = 1000):
    from random import randint, sample

    grid = [[0] * cols] * rows

    for row in grid:
        idx = sample(range(0, rows), randint(0, int(cols * 0.05)))
        for i in idx:
            row[i] = 1

    grid[0][0] = 0
    grid[rows - 1][cols - 1] = 0
    return grid


def print_grid(grid) -> None:
    print("Input Grid:")
    for row in grid:
        print("     ", end="")
        for element in row:
            print(f"{element}  ", end="")
        print("")


def get_num_of_paths(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])
    memo = {}

    def get_num_paths(x: int, y: int) -> int:
        if f"{x}{y}" in memo:
            return memo[f"{x}{y}"]
        if x >= rows or y >= cols:
            return 0
        if grid[x][y] == 1:
            return 0
        if x == rows - 1 and y == cols - 1:
            return 1

        ways = get_num_paths(x + 1, y) + get_num_paths(x, y + 1)
        memo[f"{x}{y}"] = ways
        return memo[f"{x}{y}"]

    return get_num_paths(x=0, y=0)


def main() -> None:
    grids = [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 1], [1, 0, 0]],
        [[0, 0, 1], [0, 0, 1], [1, 0, 0], [0, 0, 0]],
        [[0, 1], [0, 0]],
        # create_random_large_grid(10, 10),
        # create_random_large_grid(50, 50),
        # create_random_large_grid(100, 100),
        # create_random_large_grid(500, 500),
    ]
    outputs = [2, 2, 4, 1, -1, -1, -1, -1]

    for idx, grid in enumerate(grids):
        print_grid(grid)
        print(
            f"Expected output: {outputs[idx]}  Output: {get_num_of_paths(grid)}\n"
        )


if __name__ == "__main__":
    main()
