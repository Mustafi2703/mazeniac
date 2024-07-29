from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self,startpoint,endpoint):
        self.startpoint = startpoint
        self.endpoint = endpoint 

    def draw(self,canvas,fill_color):
        x1 = self.startpoint.x
        y1 = self.startpoint.y
        x2 = self.endpoint.x
        y2 = self.endpoint.y
        canvas.create_line(x1, y1, x2, y2, fill = fill_color,width = 2)

class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.__root.title("My window")
        self.canvas = Canvas(self.__root, width = width, height = height)
        self.canvas.pack(fill=BOTH, expand = True)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def draw_line(self,line,fill_color = "black"):
        line.draw(self.canvas,fill_color)

    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
