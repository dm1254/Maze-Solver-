from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver") 
        self.canvas = Canvas(self.root, width = self.width, height = self.height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color):
        if fill_color == "background":
            fill_color = self.canvas.cget("background")
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point 
        self.end_point = end_point
  
    def draw(self, canvas, fill_color):
        canvas.create_line(self.start_point.x, self.start_point.y, self.end_point.x,self.end_point.y, fill = fill_color, width = 2)

