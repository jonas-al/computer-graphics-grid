from math import comb

def Bezier(selected_cells, rendered_cells):
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

    return rendered_cells
