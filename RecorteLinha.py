from grid import Grid

# Função de recorte de linha
def recorte_linha(selected_cells, rendered_cells, parameters):
    x_min = min(cell[0] for cell in selected_cells)
    x_max = max(cell[0] for cell in selected_cells)
    y_min = min(cell[1] for cell in selected_cells)
    y_max = max(cell[1] for cell in selected_cells)
    
    for cell in rendered_cells:
        x, y = cell
        if ((x_min <= x and x <= x_max) and (y_min <= y and y <= y_max)):
            continue
        grid.clear_cell((x, y))
    

# Inicializar a grade
grid = Grid(extent=10, size=500)

# Adicionar o algoritmo de recorte de linha
grid.add_algorithm('Recorte de Linha', parameters=None, algorithm=recorte_linha)

# Exibir a grade
grid.show()

