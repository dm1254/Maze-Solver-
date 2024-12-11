from display import *

class Cell:
    def __init__(self,win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None 
        self._win = win
        self.visited = False 
 
    
    def draw(self, x1, y1, x2,y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2 
   
        if self._win is None:
            return 
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "background")

        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "background")

        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "background")

               
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "background")

    def draw_move(self, to_cell, undo=False):
        center1_x = (self._x1 + self._x2)/2
        center1_y = (self._y1 + self._y2)/2
        center2_x = (to_cell._x1 + to_cell._x2) / 2
        center2_y = (to_cell._y1 + to_cell._y2)/ 2
        line = Line(Point(center1_x,center1_y),Point(center2_x,center2_y))
        if undo is False:
            self._win.draw_line(line, "red")
        
        else:
            self._win.draw_line(line, "gray")

    
