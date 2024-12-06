import pygame

class Board:
    #difficulty is gonna be a number, easy = 1, med = 2, hard = 3
    def init(self, width, height, screen, difficulty):
        sudoku = SudokuGenerator(9, 20+(difficulty10))
        sudoku.fill_values()
        self.key = sudoku.get_board()
        sudoku.remove_cells()
        self.vals = sudoku.get_board()

        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.cells = []
        cell_row = []
        for i in range(0,9):
            for j in range(0,9):
                cell_row.append(Cell(self.vals[i][j], i, j, self.screen))
            self.cells.append(cell_row)
            cell_row = []
        self.selected = [0,0]

    def draw(self):
        self.screen.fill((154, 206, 235))
        while True:
            for i in range(1,9):
                if (i%3) == 0:
                    pygame.draw.line(self.screen, (0, 0, 0), (0, i (self.height / 9)),(self.width, i * (self.height / 9)), 3)
                    pygame.draw.line(self.screen, (0, 0, 0), (i * (self.width / 9), 0),(i * (self.width / 9), self.height), 3)
                pygame.draw.line(self.screen, (0, 0, 0), (0, i(self.height/9)), (self.width, i(self.height/9)))
                pygame.draw.line(self.screen, (0,0,0), (i(self.width/9), 0), (i(self.width/9), self.height))
            for row in self.cells:
                for cell in row:
                    cell.draw(self.width, self.height)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.display.update()
    def select(self, row, col):
            self.cells[row][col].selected = True
            self.selected = [row, col]
    
    def click(self, x, y):
        if (x<= self.width) and (y <=self.height):
            row = int(x/(self.width/9))
            col = int(y/(self.height/9))
            return (row, col)
        return None
    
    def clear(self):
        #sets cell value of selected cell to 0
        if self.vals[self.selected[0]][self.selected[1]] == 0:
            self.cells[self.selected[0]][self.selected[1]].set_cell_value(0)
    
    def sketch(self, value):
        # sets sketch value of selected cell to value
        self.cells[self.selected[0]][self.selected[1]].set_sketched_value(value)
        self.cells[self.selected[0]][self.selected[1]].draw(self.width, self.height)
    def place_number(self, value):
        # sets cell value of selected cell to value
        self.cells[self.selected[0]][self.selected[1]].set_cell_value(value)
    def reset_to_original(self):
        for i in range(0,9):
            for j in range(0,9):
                self.cells[i][j].set_cell_value(self.vals[i][j])
    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True
    def update_board(self):
        while True:
            for row in self.cells:
                for cell in row:
                    cell.draw(self.width, self.height)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            pygame.display.update()
    
    def find_empty(self):
        for i in range(0,9):
            for j in range(0,9):
                if self.cells[i][j].value == 0:
                    return (i,j) 
    def check_board(self):
            #check if board is solved correctly
            for i in range(0,9):
                for j in range(0,9):
                    if self.vals[i][j] == 0:
                        if self.cells[i][j].value != self.key[i][j]:
                            return False
            return True 