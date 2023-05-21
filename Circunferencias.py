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

# Adicione o algoritmo da circunferência à grade
grid.add_algorithm(name="Circunferência", parameters=None, algorithm=Circle)

# Exiba a grade
grid.show()