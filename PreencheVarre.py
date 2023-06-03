from grid import Grid

# Create a grid of extent 5 and size 600
grid = Grid(extent=10, size=500)



def fill_polygon(selected_cells, rendered_cells, parameters):
    min_x = min(cell[0] for cell in selected_cells)
    max_x = max(cell[0] for cell in selected_cells)
    min_y = min(cell[1] for cell in selected_cells)
    max_y = max(cell[1] for cell in selected_cells)

    # Inclui todas as coordenadas dos vértices na lista de células selecionadas
    for vertex in selected_cells:
        rendered_cells.append(vertex)

    # Itera por cada linha vertical dentro do polígono
    for y in range(min_y, max_y + 1):
        intersections = []

        # Verifica a interseção de cada aresta do polígono com a linha atual
        for i in range(len(selected_cells)):
            current_cell = selected_cells[i]
            next_cell = selected_cells[(i + 1) % len(selected_cells)]

            if (current_cell[1] <= y < next_cell[1]) or (next_cell[1] <= y < current_cell[1]):
                # Calcula a interseção entre a aresta e a linha
                if current_cell[1] != next_cell[1]:
                    x = current_cell[0] + (next_cell[0] - current_cell[0]) * (y - current_cell[1]) / (next_cell[1] - current_cell[1])
                else:
                    x = current_cell[0]

                intersections.append(x)

        # Ordena as interseções
        intersections.sort()

        # Preenche as células entre as interseções
        for i in range(0, len(intersections), 2):
            start_x = max(min_x, int(intersections[i]))
            end_x = min(max_x, int(intersections[i + 1]))

            for x in range(start_x, end_x + 1):
                cell = (x, y)
                rendered_cells.append(cell)

    # # Remove todas as coordenadas adicionadas anteriormente
    # for _ in range(len(selected_cells)):
    #     rendered_cells.pop()

    for cell in rendered_cells:
        grid.render_cell(cell)

    return

def fill_polygon_recursive(selected_cells, rendered_cells, parameters):
    min_x = min(cell[0] for cell in selected_cells)
    max_x = max(cell[0] for cell in selected_cells)
    min_y = min(cell[1] for cell in selected_cells)
    max_y = max(cell[1] for cell in selected_cells)

    # Inclui todas as coordenadas dos vértices na lista de células selecionadas
    for vertex in selected_cells:
        rendered_cells.append(vertex)

    # Define a função recursiva para preencher as células
    def fill_recursive(y):
        intersections = []

        # Verifica a interseção de cada aresta do polígono com a linha atual
        for i in range(len(selected_cells)):
            current_cell = selected_cells[i]
            next_cell = selected_cells[(i + 1) % len(selected_cells)]

            if (current_cell[1] <= y < next_cell[1]) or (next_cell[1] <= y < current_cell[1]):
                # Calcula a interseção entre a aresta e a linha
                if current_cell[1] != next_cell[1]:
                    x = current_cell[0] + (next_cell[0] - current_cell[0]) * (y - current_cell[1]) / (next_cell[1] - current_cell[1])
                else:
                    x = current_cell[0]

                intersections.append(x)

        # Ordena as interseções
        intersections.sort()

        # Preenche as células entre as interseções
        for i in range(0, len(intersections), 2):
            start_x = max(min_x, int(intersections[i]))
            end_x = min(max_x, int(intersections[i + 1]))

            for x in range(start_x, end_x + 1):
                cell = (x, y)
                rendered_cells.append(cell)

        if y < max_y:
            fill_recursive(y + 1)

    # Chama a função recursiva para preencher as células
    fill_recursive(min_y)
    
    for cell in rendered_cells:
        grid.render_cell(cell)

    return

grid.add_algorithm("Algoritmo recursivo", parameters=None, algorithm=fill_polygon_recursive)
grid.add_algorithm('Fill Polygon', parameters=None, algorithm=fill_polygon)
grid.show()