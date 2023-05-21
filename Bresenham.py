from grid import Grid

# Initialize grid
grid = Grid(extent=10, size=500)


def bresenham_algorithm(selected_cells, rendered_cells, parameters):
    if len(selected_cells) < 2:
        return

    
    x1, y1 = selected_cells[0]
    x2, y2 = selected_cells[1]

    #algoritmo de Bresenham
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    y = y1
    inc = 1 if y2 > y1 else -1
    D = 2 * dy - dx

    for x in range(x1, x2 + 1):
        if steep:
            rendered_cells.append((y, x))
        else:
            rendered_cells.append((x, y))
        if D >= 0:
            y += inc
            D -= 2 * dx
        D += 2 * dy

    # Renderize as células na grade
    for cell in rendered_cells:
        grid.render_cell(cell)


grid.add_algorithm(name="Bresenham", parameters=None, algorithm=bresenham_algorithm)               

grid.show()
