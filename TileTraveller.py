#Fannar Hrafn Haraldsson
#Tile Traveller
#Fannar Hrafn Haraldsson
#Tile Traveller

#grid:
grid = [
    [ ["(E)ast or (S)outh","x"], ["(E)ast or (W)est","x"], ["(S)outh or (W)est","x"] ],
    [ ["(N)orth or (E)ast or (S)outh","x"], ["(S)outh or (W)est","x"], ["(N)orth or (S)outh","x"]],
    [ ["(N)orth","o"], ["(N)orth","x"], ["(N)orth","x"]]
]


def travel_options(curr_pos,grid):
    return grid[curr_pos[0]][curr_pos[1]][0]

def travel_printer(travel_string):
    return print("You can travel: " + travel_string + ".")

def get_direction(travel_string):
    while True:
        direction = input("Direction: ")
        if direction.upper() in travel_string:
            return direction.upper()
        else:
            print("Not a valid direction!")

def new_pos(curr_pos,direction,grid):
    grid[curr_pos[0]][curr_pos[1]][1] = "x"
    if direction == "N":
        curr_pos[0] -= 1
    elif direction == "S":
        curr_pos[0] += 1
    elif direction == "E":
        curr_pos[1] += 1
    elif direction == "W":
        curr_pos[1] -= 1
    grid[curr_pos[0]][curr_pos[1]][1] = "o"
    return curr_pos, grid


curr_pos = [2,0]
#prints N
#print(grid[curr_pos[0]][curr_pos[1]][0])

while True:
    travel_string = travel_options(curr_pos,grid)
    travel_printer(travel_string)
    direction = get_direction(travel_string)
    curr_pos, grid = new_pos(curr_pos,direction,grid)
    if grid[curr_pos[0]][curr_pos[1]] == grid[2][2]:
        print("Victory!")
        break