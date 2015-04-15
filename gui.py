# Simple enough, just import everything from tkinter.
from tkinter import *
import math


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_win()

    #Creation of init_window
    def init_win(self):

        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)
        file.add_command(label="Repaint", command=self.client_repaint)

        #added "file" to our menu
        menu.add_cascade(label="Draw", menu=file)

        self.canvas=Canvas(self.master, width=500, height=500)
        self.canvas.pack()

    def client_exit(self):
        exit()
    def client_repaint(self):
        self.canvas.create_line(250, 500, 250, 500-128)
        self.draw(self.canvas, 250, 500-128, 128*0.8, 90, 10) 

    def draw(self, Canvas, x, y, length, direction, depth):
        #print(direction)
        if depth==0: #base case
            return
        end_x = x + length * (math.cos(math.radians(direction+30)))
        end_y = y - length * (math.sin(math.radians(direction+30)))
        self.canvas.create_line(x,y, end_x, end_y)
        self.draw(self.canvas, end_x, end_y, length*0.8, direction+30, depth-1) 

        end_x = x + length * (math.cos(math.radians(direction-30)))
        end_y = y - length * (math.sin(math.radians(direction-30)))
        self.canvas.create_line(x,y, end_x, end_y)
        self.draw(self.canvas, end_x, end_y, length*0.8, direction-30, depth-1) 
root = Tk()
root.geometry("500x500")
app = Window(root)
#mainloop
root.mainloop()
