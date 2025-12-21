import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

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

    def draw_velocity(self, id, n):
        xpos_list = np.array([1])*self.pxs + self.pxs/2
        ypos_list = np.array([4])*self.pxs
        x_angle_list = [1]
        y_angle_list = [0]
        if (id // n) % 2 == 0:
            self.ax.quiver(xpos_list, ypos_list, x_angle_list, y_angle_list, )
        elif (id // n) % 2 == 1:
            self.ax.quiver([[id*self.pxs], [id // n * self.pxs]], [0], [1])


    def show(self):
        plt.show()
    


l = Lattice(10, 10)
l.draw_grid()
l.draw_cell(0,5)
l.draw_cell(2,6)
l.draw_velocity(100, 10)
l.show()

@dataclass
class Velocity:
    vel: float
    is_vertical: bool
    pos: list[int, int]




class Cell:
    def __init__(self, id: int, n: int):

        self.vels: list[Velocity] = [] # right, up, left, down
        
        
        self.pressure = 0

    def get_div(self):
        return sum(self.vels)
    

class VelocityHandler:
    def __init__(self, grid_size: list[int, int], pxs: int):
        self.vels: list[Velocity] = []
        self.width = grid_size[0]
        self.height = grid_size[1]
        self.pxs = pxs

        self._init_vels()


    def _init_vels(self):
        for i in range(self.height):
            if i % 2 == 0:
                for j in range(self.width):
                    self.vels.append(Velocity(0, False, [i*self.pxs+self.pxs//2, j*self.pxs]))
            else:
                for j in range(self.width+1):
                    self.vels.append(Velocity(0, True, [i*self.pxs, j*self.pxs+self.pxs//2]))
    
    def _get_vel_obj(self, id: int) -> Velocity:
        return self.vels[id]
    

    def append_vel_objs_to_cell(self, cell: Cell)-> None:
        vel_id = cell.id//self.width*(2*self.width+1)+cell.id%self.width
        cell.vels = [self._get_vel_obj(vel_id), 
                     self._get_vel_obj(vel_id+self.width), 
                     self._get_vel_obj(vel_id+self.width+1), 
                     self._get_vel_obj(vel_id+2*self.width+1)]