#Fannar Hrafn Haraldsson
#Tile Traveller
#Fannar Hrafn Haraldsson
#Tile Traveller
#https://github.com/FannarHrafn/T-111-PROG-Assignment-8/blob/master/TileTraveller.py

#grid contains x and o because I initially planned to print out the grid
#but project doesn't want it, but its easy to add now in the future
grid = [
    [ ["(E)ast or (S)outh","x"],            ["(E)ast or (W)est","x"],   ["(S)outh or (W)est","x"] ],
    [ ["(N)orth or (E)ast or (S)outh","x"], ["(S)outh or (W)est","x"],  ["(N)orth or (S)outh","x"]],
    [ ["(N)orth","o"],                      ["(N)orth","x"],            ["(N)orth","x"]]
]

#fetches string of possible paths
def travel_options(curr_pos,grid):
    return grid[curr_pos[0]][curr_pos[1]][0]

#prints string of valid directions
def travel_printer(travel_string):
    return print("You can travel: " + travel_string + ".")

#ask user for direction until user inputs a valid direction
def get_direction(travel_string):
    while True:
        direction = input("Direction: ")
        if direction.upper() in travel_string:
            return direction.upper()
        else:
            print("Not a valid direction!")

#moves position to new position and returns the new pos and grid with changes
def new_pos(curr_pos,direction,grid):
    #remove old position
    grid[curr_pos[0]][curr_pos[1]][1] = "x"
    #change positional list according to direction
    # no need to test if we're going out of bounds as we know
    # that only legal moves make it in here because of get_direction checking them
    if direction == "N":
        curr_pos[0] -= 1
    elif direction == "S":
        curr_pos[0] += 1
    elif direction == "E":
        curr_pos[1] += 1
    elif direction == "W":
        curr_pos[1] -= 1
    #mark new position
    grid[curr_pos[0]][curr_pos[1]][1] = "o"
    return curr_pos, grid

#starting position
curr_pos = [2,0]

while True:
    #get string of possible paths
    travel_string = travel_options(curr_pos,grid)
    #print paths
    travel_printer(travel_string)
    #get direction from user
    direction = get_direction(travel_string)
    #make a new curr_pos and change the position on the grid
    curr_pos, grid = new_pos(curr_pos,direction,grid)
    
    if grid[curr_pos[0]][curr_pos[1]] == grid[2][2]:
        print("Victory!")
        break