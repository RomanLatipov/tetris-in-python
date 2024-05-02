class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_columns = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_columns)] for i in range(self.num_rows)]
        
        # [
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,0,0,0]
        # ]
        
    
    def print_grid(self):
        for row in range(self.num_rows):
            for columns in range(self.num_columns):
                print(self.grid[row][columns], end = " ")
            print()