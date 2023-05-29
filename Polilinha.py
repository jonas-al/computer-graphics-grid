from grid import Grid

# Initialize grid
grid = Grid(extent=10, size=500)

def Polilinha(selected_cells, rendered_cells, parameters):
    if len(selected_cells) < 3:
            return
    
    for i in range(0, len(selected_cells) - 2):

        
        x1, y1 = selected_cells[i]
        x2, y2 = selected_cells[i + 1]

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if x1 < x2:
            sx = 1
        else:
            sx = -1

        if y1 < y2:
            sy = 1
        else:
            sy = -1
        
        erro = dx - dy

        while x1 != x2 or y1 != y2:
            rendered_cells.append((x1, y1))
            erro2 = 2 * erro

            if erro2 > -dy:
                erro -= dy
                x1 += sx
            
            if erro2 < dx:
                erro += dx
                y1 += sy

     # Renderize as células na grade
    for cell in rendered_cells:
        grid.render_cell(cell)


grid.add_algorithm(name="Polilinha", parameters=None, algorithm=Polilinha)
grid.show()