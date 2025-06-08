def make_empty_char_grid(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]

def place_dot(grid, r, c):
    grid[r][c] = '●'

def connect_vertically(grid, r1, r2, c):
    for r in range(min(r1, r2) + 1, max(r1, r2)):
        grid[r][c] = '|'

def connect_horizontally(grid, r, c1, c2):
    for c in range(min(c1, c2) + 1, max(c1, c2)):
        grid[r][c] = '-'

def draw_letter(letter_coords, row_offset, col_offset, grid):
    # Place dots and connections
    placed = set()
    for (r, c) in letter_coords:
        pr, pc = r * 2, c * 2
        place_dot(grid, pr + row_offset, pc + col_offset)
        placed.add((pr + row_offset, pc + col_offset))

    for (r, c) in letter_coords:
        pr, pc = r * 2 + row_offset, c * 2 + col_offset
        # check vertical neighbors
        for dr in [-1, 1]:
            neighbor = (pr + dr * 2, pc)
            if neighbor in placed:
                connect_vertically(grid, pr, neighbor[0], pc)
        # check horizontal neighbors
        for dc in [-1, 1]:
            neighbor = (pr, pc + dc * 2)
            if neighbor in placed:
                connect_horizontally(grid, pr, pc, neighbor[1])

def print_grid(grid):
    for row in grid:
        print("".join(row))

# Define 3x2 dot coordinates for H and I
letter_H = [(0,0), (1,0), (2,0), (1,1), (0,1), (2,1)]
letter_I = [(0,1), (1,1), (2,1)]

# Setup grid
rows = 3 * 2 - 1  # 3 dot rows with spacing
cols = 2 * 4 - 1  # 2 dots per letter, 1 spacing, 2 letters

grid = make_empty_char_grid(rows, cols)

# Draw "H"
draw_letter(letter_H, 0, 0, grid)
# Draw "I" with offset (row_offset=0, col_offset=5)
draw_letter(letter_I, 0, 5, grid)

# Print result
print_grid(grid)
