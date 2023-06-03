from grid import Grid

# Initialize grid
grid = Grid(extent=10, size=500)

def Polilinha(selected_cells, rendered_cells, parameters):
    if len(selected_cells) < 3:
        return

    for i in range(len(selected_cells) - 1):
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

        while True:
            rendered_cells.append((x1, y1))

            if x1 == x2 and y1 == y2:
                break

            e2 = 2 * erro
            if e2 > -dy:
                erro -= dy
                x1 += sx

            if e2 < dx:
                erro += dx
                y1 += sy

    rendered_cells.append(selected_cells[-1])

    # Renderize a última linha
    x_last, y_last = selected_cells[-1]
    x_prev, y_prev = selected_cells[-2]
    dx = abs(x_last - x_prev)
    dy = abs(y_last - y_prev)
    sx = 1 if x_prev < x_last else -1
    sy = 1 if y_prev < y_last else -1
    erro = dx - dy

    while True:
        rendered_cells.append((x_prev, y_prev))

        if x_prev == x_last and y_prev == y_last:
            break

        e2 = 2 * erro
        if e2 > -dy:
            erro -= dy
            x_prev += sx

        if e2 < dx:
            erro += dx
            y_prev += sy

    for cell in rendered_cells:
        grid.render_cell(cell)
    print(rendered_cells)


grid.add_algorithm(name="Polilinha", parameters=None, algorithm=Polilinha)
grid.show()