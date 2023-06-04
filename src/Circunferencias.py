import math
def Circle(selected_cells, rendered_cells):
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

    return rendered_cells