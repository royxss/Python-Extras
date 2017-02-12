# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 23:56:23 2017
Solving mazes using Python: Simple recursivity and A* search

We use a nested list of integers to represent the maze.
Diagonal movement not allowed 
The values are the following:

0: empty cell
1: unreachable cell: e.g. wall
2: ending cell
3: visited cell

@author: SROY
"""
grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]
        
# x,y -> 5,0 to 5,5
x=0; y=0  
print("Starting at (x,y)=("+ str(x) + "," + str(y)+")")
steps = 0  # Counting the steps
visited = 3 # Visited Flag
check = 8 # Check flag when we have two routes

while (1==1):
    # One move per counter
    # to reach 5,5 lets consider down and right movement preference
    # This preference will only be reversed based on relative distance

    if (x < 5 and grid[x+1][y] == 0) and (y <5 and grid[x][y+1] == 0):
        # Two routes confusion
         grid[x][y] = visited
         print("Two routes confusion at ("+ str(x) + "," + str(y)+")")
         i=0;j=0
         for i in range(6):
             for j in range(6):
                 if grid[i][j] == check:
                     grid[i][j] = 3 
         visited = check
         route1 = [x+1, y] #Down
         route2 = [x, y+1] #Right
         recount = steps

    # Check down cell
    if x < 5 and grid[x+1][y] == 0:
         print("down")
         grid[x][y] = visited   # Assign traversed cell to 3
         x= x+1; y = y    # Set X,Y to new Value         
         steps +=1        # Count Steps 
         continue         # Loop to next if job done

    # Check right cell
    if y < 5 and grid[x][y+1] == 0:
         print("right")
         grid[x][y] = visited 
         x= x; y = y+1
         steps +=1
         continue
         
    # Check top cell
    if x > 0 and grid[x-1][y] == 0:
         print("top")
         grid[x][y] = visited 
         x= x-1; y = y
         steps +=1
         continue
         
    # Check left cell
    if y > 0 and grid[x][y-1] == 0:
         print("left")
         grid[x][y] = visited 
         x= x; y = y-1
         steps +=1
         continue

    if (x == 5 and y < 5 and grid[x][y+1] == 2) or (x < 5 and y ==5 and grid[x+1][y] == 2):
         print("Reached at (x,y)=(5,5)")
         print ("It took " + str(steps) + " steps to reach destination")
         i=0;j=0
         for i in range(6):
             for j in range(6):
                 if grid[i][j] == check:
                     grid[i][j] = 3            
         break
     
    print("!!!Stalemate!!!")
    print("........Choose alternate route........")
    i=0;j=0
    for i in range(6):
        for j in range(6):
            if grid[i][j] == check:
                grid[i][j] = 0
    # Start route 2
    visited = 3; x = route2[0]; y = route2[1]; steps = recount
    print("........Restarting at (x,y) = ("+str(x)+","+str(y)+")")            
        

