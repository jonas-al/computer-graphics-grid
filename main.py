from grid import Grid
import math
from math import comb

#Grade
grid = Grid(extent=10, size=500)

#Algoritmo de Bresenham
def bresenham_algorithm(selected_cells, rendered_cells, parameters):
    if len(selected_cells) < 2:
        return

    x1, y1 = selected_cells[0]
    x2, y2 = selected_cells[1]

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

  
    for cell in rendered_cells:
        grid.render_cell(cell)

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
    



#Circuferência
def Circle_algorithm(selected_cells, rendered_cells, parameters):
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


    for cell in rendered_cells:
        grid.render_cell(cell)

def Polilinha_algorithm(selected_cells, rendered_cells, parameters):
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


def Bezier(selected_cells, rendered_cells, parameters):
    grauCurva = len(selected_cells) - 1

    for t in range(0, 101):
        t /= 100
        x = 0
        y = 0
        t_pot = 1

        for i in range(grauCurva + 1):
            coefBinomial = comb(grauCurva, i)
            blend = coefBinomial * pow(1 - t, grauCurva - i) * pow(t, i)

            x += selected_cells[i][0] * blend
            y += selected_cells[i][1] * blend
            t_pot *= t
        
        rendered_cells.append((int(x), int(y)))
        grid.render_cell((int(x), int(y)))



def fill_polygon_recursive(selected_cells, rendered_cells, parameters):
    min_x = min(cell[0] for cell in selected_cells)
    max_x = max(cell[0] for cell in selected_cells)
    min_y = min(cell[1] for cell in selected_cells)
    max_y = max(cell[1] for cell in selected_cells)

    def fill_recursive(y):
        intersections = []

        # Verifica a interseção de cada aresta do polígono com a linha atual
        for i in range(len(selected_cells)):
            current_cell = selected_cells[i]
            next_cell = selected_cells[(i + 1) % len(selected_cells)]

            if (current_cell[1] <= y < next_cell[1]) or (next_cell[1] <= y < current_cell[1]):
                # Calcula a interseção entre a aresta e a linha
                if current_cell[1] != next_cell[1]:
                    x = current_cell[0] + (next_cell[0] - current_cell[0]) * (y - current_cell[1]) / (
                            next_cell[1] - current_cell[1])
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


#Varredura
def fill_polygon(selected_cells, rendered_cells, parameters):
    min_x = min(cell[0] for cell in selected_cells)
    max_x = max(cell[0] for cell in selected_cells)
    min_y = min(cell[1] for cell in selected_cells)
    max_y = max(cell[1] for cell in selected_cells)

    
    for vertex in selected_cells:
        rendered_cells.append(vertex)


    for y in range(min_y, max_y + 1):
        intersections = []


        for i in range(len(selected_cells)):
            current_cell = selected_cells[i]
            next_cell = selected_cells[(i + 1) % len(selected_cells)]

            if (current_cell[1] <= y < next_cell[1]) or (next_cell[1] <= y < current_cell[1]):
      
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

    #Remove todas as coordenadas adicionadas anteriormente
    # for _ in range(len(selected_cells)):
    #     rendered_cells.pop()

    print(rendered_cells)
    for cell in rendered_cells:
        grid.render_cell(cell)


# def Varredura(selected_cells, rendered_cells, parameters):
#     min_x = min(cell[0] for cell in selected_cells)
#     max_x = max(cell[0] for cell in selected_cells)
#     min_y = min(cell[1] for cell in selected_cells)
#     max_y = max(cell[1] for cell in selected_cells)

#     # Lógica para renderizar as células entre os pontos do polígono
#     for y in range(min_y, max_y + 1):
#         intersections = []

#         # Verifica a interseção de cada aresta do polígono com a linha atual
#         for i in range(len(selected_cells)):
#             current_cell = selected_cells[i]
#             next_cell = selected_cells[(i + 1) % len(selected_cells)]

#             if (current_cell[1] <= y < next_cell[1]) or (next_cell[1] <= y < current_cell[1]):
#                 # Calcula a interseção entre a aresta e a linha
#                 if current_cell[1] != next_cell[1]:
#                     x = current_cell[0] + (next_cell[0] - current_cell[0]) * (y - current_cell[1]) / (
#                             next_cell[1] - current_cell[1])
#                 else:
#                     x = current_cell[0]

#                 intersections.append(x)

#         # Ordena as interseções
#         intersections.sort()

#         # Preenche as células entre as interseções
#         for i in range(0, len(intersections), 2):
#             start_x = max(min_x, int(intersections[i]))
#             end_x = min(max_x, int(intersections[i + 1]))
           

#             for x in range(start_x, end_x + 1):
#                 cell = (x, y)
#                 rendered_cells.append(cell)
    
#     print(rendered_cells)
#     # Renderize as células na grade
#     for cell in rendered_cells:
#         grid.render_cell(cell)

def render_selected(selected_cells, rendered_cells, parameters):
	for cell in selected_cells:
		grid.render_cell(cell)

#Renderização de células           
grid.add_algorithm('Render Selected', parameters=None, algorithm=render_selected)

#Bresenham
grid.add_algorithm(name="Bresenham", parameters=None, algorithm=bresenham_algorithm)

#Círculo               
grid.add_algorithm(name="Circunferência", parameters=None, algorithm=Circle_algorithm)

#Polilinha
grid.add_algorithm(name="Polilinha", parameters=None, algorithm=Polilinha_algorithm)

#Curva Bezier
grid.add_algorithm(name="Curva", parameters=None, algorithm=Bezier)

#Preenchimento Recursivo
grid.add_algorithm("Preenchimento Recursivo", parameters=None, algorithm=fill_polygon_recursive)

#Preenchimento
grid.add_algorithm('Varredura', parameters=None, algorithm=fill_polygon)

#Recorte linha
grid.add_algorithm('Recorte de Linha', parameters=None, algorithm=recorte_linha)

#grid.add_algorithm(name="Varredura2", parameters=None, algorithm=Varredura)

grid.show()
