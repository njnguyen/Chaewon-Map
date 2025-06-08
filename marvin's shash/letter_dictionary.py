
# all letters start bottom left except C
letters = {
    'C':[(2,0),(1,0),(0,0),(0,1),(0,2),(1,2),(2,2)],
    'H':[(0,2),(0,1),(0,0),(0,1),(1,1),(2,1),(2,2)],
    'A':[(0,2),(0,1),(0,0),(1,0),(1,1),(0,1),(1,1),(1,2)],
    'E':[(0,2),(0,1),(0,0),(1,0),(0,0),(0,1),(1,1),(0,1),(0,2),(1,2)],
    'W':[(0,2),(0,1),(0,0),(0,1),(0,2),(1,2),(1,1),(1,2),(2,2),(2,1),(2,0),(2,1),(2,2)],
    'O':[(0,2),(1,2),(1,1),(1,0),(0,0),(0,1),(0,2),(1,2),(2,2)],
    'N':[(0,2),(0,1),(0,0),(1,0),(1,1),(1,2),(2,2),(2,1),(2,0),(2,1),(2,2)]

    # 'C':[(2,0),(0,0),(0,2),(2,2)]
    # 'H':[(0,2),(0,0),(0,1),(1,1),(1,2)]
    # 'A':[(0,2),(0,0),(0,1),(1,1),(1,0),(1,1),(1,2)]
    # 'E':[(0,2),(0,0),(1,0),(0,0),(0,1),(1,1),(0,1),(0,2),(1,2)]
    # 'W':[(0,2),(0,0),(0,2),(1,2),(1,1),(1,2),(2,2),(2,0),(2,2)]
    # 'O':[(0,2),(1,2),(1,0),(0,0),(0,2),(1,2)]
    # 'N':[(0,2),(0,0),(1,0),(1,2),(2,2),(2,0),(2,2)]
}

def write_letter(letter):
    arr = letters[letter]
    for i in range(0,3):
        for j in range(0,3):
            if (j,i) in arr:
                print('X ', end="")
            else:
                print('* ', end="")
        print('\n')

def ppl(grid):
    for i in range(0,3):
        for j in range(0,3):
            if (j,i) in grid:
                print('X ', end="")
            else:
                print('* ', end="")
        print('\n')

# def ppline(grid):
#     hor, ver, dot = [], [], []
#     for i in range(0,len(grid)-1):
#         cur = grid[i]
#         target = grid[i+1]
#         print(cur)
#         print(target)
#         if cur[0]-target[0] != 0:  # horiz/vert
#             print("horiz")
#             if cur[0] > target[0]:  # move left
#
#             r = cur[1]
#         else:
#             print("vertical")


def extend_grid(arr):
    new_arr = []
    for i,j in arr:
        new_arr.append((2*i,2*j))
    return(new_arr)


def write_and_connect(letter):
    arr = letters[letter]
    new_grid = extend_grid(arr)
    # print(new_grid)
    # ppline(new_grid)




if __name__ == '__main__':
    write_letter('C')
    write_letter('H')
    write_letter('A')
    write_letter('E')
    write_letter('W')
    write_letter('O')
    write_letter('N')
    # write_and_connect('C')