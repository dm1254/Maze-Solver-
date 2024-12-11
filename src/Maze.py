from Cell import *
from display import * 
import time
import random


class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None, seed = None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self.break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_wall_r(0,0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self.num_cols):
            row = []
            for j in range(self.num_rows):
                row.append(Cell(self.win)) 
            self._cells.append(row)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self,i,j):
        if self.win is None:
            return 
        x1 = i * self.cell_size_x + self.x1
        y1 = j * self.cell_size_y + self.y1
        x2 = self.cell_size_x + x1
        y2 = self.cell_size_y + y1
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return 
        
        self.win.redraw()
        time.sleep(.05)

    def break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)
    
    def _break_wall_r(self,i,j):
        current_cell = self._cells[i][j]
        current_cell.visited = True 
        while True:
            values_to_visit = []
            if j> 0 and not self._cells[i][j-1].visited:
                    values_to_visit.append((i,j-1))
            if j < self.num_rows-1 and not self._cells[i][j+1].visited:
                    values_to_visit.append((i,j+1))
            if i > 0 and not self._cells[i-1][j].visited:
                    values_to_visit.append((i-1,j))
            if i < self.num_cols-1 and not self._cells[i+1][j].visited:
                    values_to_visit.append((i+1,j))
            if len(values_to_visit) == 0:
                self._draw_cell(i,j)
                return

        
            direction = random.randrange(len(values_to_visit))
            next_cell = values_to_visit[direction]
            
            if next_cell[1] == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            if next_cell[1]== j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if next_cell[0] == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if next_cell[0] == i+1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                
            self._break_wall_r(next_cell[0], next_cell[1])
         
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited= False

    def solve(self):
        if self.solve_r() is True:
            return True
        else:
           return False

    def solve_r(self, i = 0,j = 0):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if current_cell == self._cells[self.num_cols-1][self.num_rows-1]:
            return True
      
        directions = [(0,-1,'top'),(0,1,'bottom'),(-1,0,'left'),(1,0,'right')]
        for i2,j2,dir in directions:
            ni,nj = i+i2, j+j2
            if 0<= ni < self.num_cols and 0<=nj < self.num_rows:
                next_cell = self._cells[ni][nj]
                if not getattr(current_cell, f'has_{dir}_wall') and not next_cell.visited:
                    current_cell.draw_move(next_cell)
                    if self.solve_r(ni,nj):
                        return True
                    else:
                        current_cell.draw_move(next_cell, undo = True)
                
        return False
                     
                

