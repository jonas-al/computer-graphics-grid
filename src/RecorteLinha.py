# Função de recorte de linha
def recorte_linha(selected_cells, rendered_cells):
    x_min = min(cell[0] for cell in selected_cells)
    x_max = max(cell[0] for cell in selected_cells)
    y_min = min(cell[1] for cell in selected_cells)
    y_max = max(cell[1] for cell in selected_cells)
    
    resultado = []
    for cell in rendered_cells:
        x, y = cell
        if ((x_min <= x and x <= x_max) and (y_min <= y and y <= y_max)):
            resultado.append([x, y])
    
    return resultado

