import math
from grid import Grid

# Initialize grid
grid = Grid(extent=10, size=500)

def Circle(selected_cells, rendered_cells, parameters):
    x1, y1 = selected_cells[0]
    x2, y2 = selected_cells[1]

    def calcular_raio(x1, y1, x2, y2):
        raio = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return int(raio)

    raio = calcular_raio(x1, y1, x2, y2)

    # Lógica para renderizar as células da circunferência
    x = raio
    y = 0
    d = 1 - raio

    while x >= y:
        rendered_cells.append((x1 + x, y1 + y))
        rendered_cells.append((x1 + y, y1 + x))
        rendered_cells.append((x1 - y, y1 + x))
        rendered_cells.append((x1 - x, y1 + y))
        rendered_cells.append((x1 - x, y1 - y))
        rendered_cells.append((x1 - y, y1 - x))
        rendered_cells.append((x1 + y, y1 - x))
        rendered_cells.append((x1 + x, y1 - y))

        if d < 0:
            d = d + 2 * y + 3
        else:
            d = d + 2 * (y - x) + 5
            x = x - 1

        y = y + 1

    # Renderize as células na grade
    for cell in rendered_cells:
        grid.render_cell(cell)

grid = Grid(extent=10, size=500)

 

def Scanline(selected_cells, rendered_cells, parameters):
    if not selected_cells:
        return
     
    y_min = min(selected_cells, key=lambda cell: cell[1])[1]
    y_max = max(selected_cells, key=lambda cell: cell[1])[1]


    active_edges = []

    for y in range(y_min, y_max + 1):
       
        intersections = []

        for edge in active_edges:
            if edge['y_max'] > y:
                intersections.append(edge['x_intercept'])

        intersections.sort()

     
        for i in range(0, len(intersections), 2):
            x_start = intersections[i]
            x_end = intersections[i + 1]

           
            for x in range(x_start, x_end + 1):
                rendered_cells.append((x, y))

       
        active_edges = [edge for edge in active_edges if edge['y_max'] > y]

        for edge in active_edges:
            edge['x_intercept'] += edge['slope']

   
    for cell in rendered_cells:
        grid.render_cell(cell)

def interpolate_x(cell1, cell2, y):
    x1, y1 = cell1
    x2, y2 = cell2

    if y1 == y2:
        return min(x1, x2)

    # Calcular o valor de x usando interpolação linear
    x = x1 + ((x2 - x1) * (y - y1)) / (y2 - y1)
    return round(x)


def fill_polygon(selected_cells, rendered_cells, parameters):
    min_x = min(cell[0] for cell in selected_cells)
    max_x = max(cell[0] for cell in selected_cells)
    min_y = min(cell[1] for cell in selected_cells)
    max_y = max(cell[1] for cell in selected_cells)

    # Itera por cada linha vertical dentro do polígono
    for y in range(min_y, max_y + 1):
        intersections = []
        inside = False

        # Verifica a interseção de cada aresta do polígono com a linha atual
        for i in range(len(selected_cells)):
            current_cell = selected_cells[i]
            next_cell = selected_cells[(i + 1) % len(selected_cells)]

            if (current_cell[1] > y) != (next_cell[1] > y):
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
                if grid.is_valid_cell(cell):
                    grid.render_cell(cell)

    return

def Varredura(selected_cells, rendered_cells, parameters):
    x1, y1 = selected_cells[0]
    x2, y2 = selected_cells[1]

    def calcular_raio(x1, y1, x2, y2):
        raio = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return int(raio)

    raio = calcular_raio(x1, y1, x2, y2)

    # Lógica para renderizar as células da circunferência
    x = raio
    y = 0
    d = 1 - raio

    while x >= y:
        for i in range(y1 - y, y1 + y + 1):
            rendered_cells.append((x1 + x, i))
            rendered_cells.append((x1 - x, i))
        for i in range(y1 - x, y1 + x + 1):
            rendered_cells.append((x1 + y, i))
            rendered_cells.append((x1 - y, i))

        if d < 0:
            d = d + 2 * y + 3
        else:
            d = d + 2 * (y - x) + 5
            x = x - 1

        y = y + 1

    # Renderize as células na grade
    for cell in rendered_cells:
        grid.render_cell(cell)


# Adicione o algoritmo da circunferência à grade
grid.add_algorithm(name="Varredura", parameters=None, algorithm=Varredura)
# Adicione o algoritmo de preenchimento Scanline à grade
grid.add_algorithm(name="Scanline", parameters=None, algorithm=Scanline)


# Adicione o algoritmo da circunferência à grade
grid.add_algorithm(name="Circunferência", parameters=None, algorithm=Circle)
grid.add_algorithm('Fill Polygon', parameters=None, algorithm=fill_polygon)

# Exiba a grade
grid.show()