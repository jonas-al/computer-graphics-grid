from math import comb
from grid import Grid

# Initialize grid
grid = Grid(extent=10, size=500)

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

grid.add_algorithm(name="Curva", parameters=None, algorithm=Bezier)
grid.show()
