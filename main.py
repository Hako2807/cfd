from lattice import Velocity, VelocityHandler, Lattice, Cell, CellHandler

def main():
    width = 20
    height = 20
    pxs = 40

    l = Lattice(width, height, pxs)
    vel_handler = VelocityHandler([width, height], pxs)
    cell_handler = CellHandler([width, height])
    
    l.draw_grid()
    for cell in cell_handler.cells:
        vel_handler.append_vel_objs_to_cell(cell)


    print(f"{cell_handler.cells[0].get_flux()}, {cell_handler.cells[1].get_flux()}, {vel_handler.vels[width+1].vel}, {cell_handler.cells[0].get_flux()+cell_handler.cells[1].get_flux()}")
    vel_handler.vels[width+1].vel = 1
    print(f"{cell_handler.cells[0].get_flux()}, {cell_handler.cells[1].get_flux()}, {vel_handler.vels[width+1].vel}, {cell_handler.cells[0].get_flux()+cell_handler.cells[1].get_flux()}")


    for i in range(width * height):
        l.draw_cell(i, cell_handler)
    
    l.draw_velocity(vel_handler)

    l.show()

    return

if __name__ == "__main__":
    main()