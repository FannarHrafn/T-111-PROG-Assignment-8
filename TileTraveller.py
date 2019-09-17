#Fannar Hrafn Haraldsson
#Tile Traveller
#Fannar Hrafn Haraldsson
#Tile Traveller

#grid:
grid = [
    [ ["NE","x"], ["WE","x"], ["WS","x"] ],
    [ ["NSE","x"], ["SW","x"], ["NS","x"]],
    [ ["N","o"], ["N","x"], ["N","x"]]
]

curr_pos = [2,0]
#prints N
#print(grid[curr_pos[0]][curr_pos[1]][0])

def travel_options(curr_pos,grid):
    templist = []
    for x in grid[curr_pos[0]][[curr_pos[1]]][0]
        templist.append(x)
    return templist




while True:
    travellist = travel_options(curr_pos,grid)
    direction = get_direction()
    curr_pos = new_pos(curr_pos,direction)