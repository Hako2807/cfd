from lattice import Velocity, VelocityHandler, Lattice, Cell, CellHandler

def main():
    width = 20
    height = 10
    pxs = 10

    l = Lattice(width, height, pxs)
    vel_handler = VelocityHandler([width, height], pxs)
    cell_handler = CellHandler([width, height])

    for cell in cell_handler.cells:
        vel_handler.append_vel_objs_to_cell(cell)



    l.draw_grid()
    l.draw_velocity(vel_handler)
    l.show()

    return

if __name__ == "__main__":
    main()