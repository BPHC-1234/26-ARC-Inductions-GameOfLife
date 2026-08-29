

#---------------------------- TASK 1 ----------------------------


    
    
    #Row-20,Col-35
    #Underpopulation: Any live cell with fewer than two live neighbors dies.
    #Survival: Any live cell with two or three live neighbors lives on to the next generation.
    #Overpopulation: Any live cell with more than three live neighbors dies.
    #Reproduction: Any dead cell with exactly three live neighbors becomes a live cell.
        
def count_neighbors(grid, row, col):
       alive_count=0                            


       for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if r==row and c==col:                       # code to prevent counting the given cell as its own neightbor
                    continue
                if r<0 or c<0 or r>=len(grid) or c>=len(grid[r]):   #helps in avoiding error due to 'edge cases'
                    continue
                
                if grid[r][c]==1:
                    alive_count+=1
       return alive_count

        
        
        
"""Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
    
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    
    
    # TODO: Implement your neighbor-counting logic here!



#---------------------------- TASK 2 ----------------------------

"""
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
def compute_next_generation(grid):   
       rows = len(grid)
       cols = len(grid[0]) if rows > 0 else 0
    
    # Create a new blank grid of the same size, filled with 0s (dead cells)
       next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
       for r in range(rows):
          
           for c in range(cols):
                  alive_count=count_neighbors(grid,r,c)
                  if grid[r][c]==1 and alive_count<2:#Underpopulation
                         next_grid[r][c]=0
                  if grid[r][c]==1 and alive_count in [2,3]:#Survival
                         next_grid[r][c]=1

                  if grid[r][c]==1 and alive_count>3:#Overpopulation
                         next_grid[r][c]=0
                         
                  if grid[r][c]==0 and alive_count==3:#Reproduction
                         next_grid[r][c]=1
       return next_grid
                         
    
    # TODO: Iterate through every cell in the `grid`.
    # TODO: Use your `count_neighbors` function to find out how many neighbors it has.
    # TODO: Apply the 4 Rules of Life to determine if it should be 1 (alive) or 0 (dead) in `next_grid`.

    
    

