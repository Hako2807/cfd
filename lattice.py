import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pchs
from dataclasses import dataclass

@dataclass
class Velocity:
    vel: float
    is_vertical: bool
    pos: list[int, int]


class Cell:
    def __init__(self, id: int):
        self.vels: list[Velocity] = [] # right, up, left, down
        self.id = id

        self.pressure = 0

    def get_flux(self):
        return self.vels[0].vel + self.vels[1].vel - self.vels[2].vel - self.vels[3].vel
    
    

class VelocityHandler:
    def __init__(self, grid_size: list[int, int], pxs: int):
        self.vels: list[Velocity] = []
        self.width = grid_size[0]
        self.height = grid_size[1]
        self.pxs = pxs

        self._init_vels()


    def _init_vels(self):
        for i in range(2*self.height+1):
            if i % 2 == 1:
                for j in range(self.width+1):
                    self.vels.append(Velocity(np.random.random()-0.5, False, [j*self.pxs, i//2*self.pxs+ self.pxs//2]))
            else:
                for j in range(self.width):
                    self.vels.append(Velocity(np.random.random()-0.5, True, [j*self.pxs+ self.pxs//2, i//2*self.pxs]))
    
    def _get_vel_obj(self, id: int) -> Velocity:
        # print(id, len(self.vels))
        return self.vels[id]
    

    def append_vel_objs_to_cell(self, cell: Cell)-> None:
        vel_id = cell.id//self.width*(2*self.width+1)+cell.id%self.width
        cell.vels = [self._get_vel_obj(vel_id), 
                     self._get_vel_obj(vel_id+self.width), 
                     self._get_vel_obj(vel_id+self.width+1), 
                     self._get_vel_obj(vel_id+2*self.width+1)]
        
class CellHandler:
    def __init__(self, grid_size: list[int, int]):
        self.cells = []
        self.width = grid_size[0]
        self.height = grid_size[1]

        self._make_cells()

    def _make_cells(self):
        for i in range(self.width*self.height):
            self.cells.append(Cell(i))




class Lattice:
    def __init__(self, width: int, height: int, pxs: int) -> None:
        self.width: int = width
        self.height: int = height
        self.pxs: int = pxs

        self.fig, self.ax = plt.subplots()


    def draw_grid(self) -> None:
        for i in range(self.width+1):
            self.ax.plot([i*self.pxs]*2, [0, self.pxs*self.height], "r")

        for i in range(self.height+1):
            self.ax.plot([0, self.pxs*self.width], [i*self.pxs]*2, "r")
    
    def draw_cell(self, id, cell_handler):
        c = 0.5- cell_handler.cells[id].get_flux()/8
        # c = 1 if cell_handler.cells[id].get_flux() > 0 else 0.5
        rect = pchs.Rectangle((id % self.width * self.pxs,id // self.width*self.pxs), self.pxs, self.pxs, color=(c, 0.8, 0.1))
        self.ax.add_patch(rect)
        self.ax.text(id % self.width * self.pxs+ self.pxs//4, id // self.width*self.pxs+ self.pxs//4, f"{cell_handler.cells[id].get_flux():.1f}")

    def draw_velocity(self, vel_handler: VelocityHandler):
        xpos_list = []
        ypos_list = []
        x_angle_list = []
        y_angle_list = []

        for vel in vel_handler.vels:
            xpos_list.append(vel.pos[0])
            ypos_list.append(vel.pos[1])
            x_angle_list.append(int(not vel.is_vertical)*vel.vel)
            y_angle_list.append(int(vel.is_vertical)*vel.vel)
        
        self.ax.quiver(xpos_list, ypos_list, x_angle_list, y_angle_list)


    def show(self):
        self.ax.set_aspect("equal")
        plt.show()
    