import numpy as np
import matplotlib.pyplot as plt

class Lattice:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height

        self.pxs = 10
        self.fig, self.ax = plt.subplots()


    def draw_grid(self) -> None:
        for i in range(self.width+1):
            self.ax.plot([0, self.pxs*self.height], [i*self.pxs]*2, "r")
        for i in range(self.height+1):
            self.ax.plot([i*self.pxs]*2, [0, self.pxs*self.width], "r")

    
    def draw_cell(self, i, j):
        self.ax.plot(i*self.pxs+ self.pxs/2, j * self.pxs + self.pxs/2, "bo")

    
    def show(self):
        plt.show()
    


l = Lattice(10, 10)
l.draw_grid()
l.draw_cell(0,5)
l.draw_cell(2,6)
l.show()

class Cell:
    def __init__(self):
        self.vels = np.array([0,0,0,0]) # right, up, left, down
        self.pressure = 0
