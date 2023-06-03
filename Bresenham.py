from grid import Grid

# Initialize grid
grid = Grid(extent=10, size=500)

# Função de recorte de linha
def recorte_linha(selected_cells, rendered_cells, parameters):
    if not selected_cells:
        return

    x_min = min(cell[0] for cell in selected_cells)
    x_max = max(cell[0] for cell in selected_cells)
    y_min = min(cell[1] for cell in selected_cells)
    y_max = max(cell[1] for cell in selected_cells)
    
    for cell in rendered_cells:
        x, y = cell
        if ((x_min <= x <= x_max) and (y_min <= y <= y_max)):
            continue
        grid.clear_cell((x, y))
    


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
    # Recorte da linha
    recorte_linha(selected_cells, rendered_cells, parameters)
    # Renderize as células na grade
    for cell in rendered_cells:
        grid.render_cell(cell)


grid.add_algorithm(name="Bresenham", parameters=None, algorithm=bresenham_algorithm)               

# Adicionar o algoritmo de recorte de linha
grid.add_algorithm('Recorte de Linha', parameters=None, algorithm=recorte_linha)
grid.show()
