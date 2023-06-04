def preencher_linha_horizontal(x1, x2, y, rendered_cells):
    for x in range(x1, x2):
        rendered_cells.append((x, y))


def PreenchePoligno(selected_cells, rendered_cells):
    max_y = max(cell[1] for cell in selected_cells)
    min_y = min(cell[1] for cell in selected_cells)

    pontosIntersecao = []

    for i in range(0, len(selected_cells) - 1):
        x1, y1 = selected_cells[i]
        if selected_cells[0][1]:
            x2, y2 = selected_cells[0]
        else:
            x2, y2 = selected_cells[i + 1]

        if y1 != y2:
            pontosIntersecao.append((min(x1, x2), (y1, y2)))

    for y in range(min_y, max_y):
        LinhasIntersecao = []

        for (x1, (y1, y2)) in pontosIntersecao:
            if y1 <= y < y2 or y2 <= y < y1:
                x_intersecao = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                LinhasIntersecao.append(x_intersecao)

        LinhasIntersecao.sort()

        for i in range(0, len(LinhasIntersecao) - 1, 2):
            x_inicio = LinhasIntersecao[i]
            x_fim = LinhasIntersecao[i + 1]
            preencher_linha_horizontal(int(x_inicio), int(x_fim), y, rendered_cells)

    return rendered_cells
