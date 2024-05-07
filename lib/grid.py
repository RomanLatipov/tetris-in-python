from lib.settings import *
from lib.score import Score

class Grid:
    def __init__(self):
        self.num_rows = rows
        self.num_columns = columns
        self.cell_size = cell_size
        self.colors = colors()
        self.grid = [[0 for j in range(self.num_columns)] for i in range(self.num_rows)]

        self.current_level = 1
        self.current_score = 0
        self.current_lines = 0

        self.score = Score()

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                cell_rect = pygame.Rect(column*self.cell_size+1, row*self.cell_size+1, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[self.grid[row][column]], cell_rect)

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_columns:
            return True
        return False
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_columns):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.num_columns):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        for column in range(self.num_columns):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0
    
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
                self.calculate_score(completed)

    def calculate_score(self, num_lines):
        self.current_lines += num_lines
        self.current_score += score_data[num_lines] * self.current_level

        #  every 10 lines the level goes up by 1
        if self.current_level / 10 > self.current_level:
            self.current_level += 1
        #     self.down_speed *= 0.75
        #     self.down_speed_faster = self.down_speed * 0.3
        #     self.timers['vertical move'].duration = self.down_speed
        self.score.update_score(2, 40, 1)
        # self.update_score(self.current_lines, self.current_score, self.current_level)
    
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                self.grid[row][column] = 0