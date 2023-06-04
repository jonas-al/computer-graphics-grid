import numpy as np
from src.Polilinha import polilinha

def translacao(rendered_cells, parameters):
    pontos = rendered_cells
    pontos_deslocamento = parameters['Ponto de Deslocamento'].split(',')
    pontos_deslocamento = [int(ponto) for ponto in pontos_deslocamento]

    resultado = []
    for cell in pontos:
        x, y = cell
        resultado.append((x + pontos_deslocamento[0], y + pontos_deslocamento[1]))
    
    return resultado

def escala(selected_cells, parameters):
    pontos = selected_cells
    ponto_fixo = parameters['Ponto Fixo'].split(',')
    ponto_fixo = [int(ponto) for ponto in ponto_fixo]
    fator_x = int(parameters['Fator X'])
    fator_y = int(parameters['Fator Y'])

    pontos_escala = []
    for ponto in pontos:
        x = ponto[0]
        y = ponto[1]
        escala_x = ponto_fixo[0] + (x - ponto_fixo[0]) * fator_x
        escala_y = ponto_fixo[1] + (y - ponto_fixo[1]) * fator_y
        ponto_escala = (escala_x, escala_y)
        pontos_escala.append(ponto_escala)
    
    pontos_escala = polilinha(pontos_escala)
    return pontos_escala

def rotacao(rendered_cells, parameters):
    pontos = rendered_cells
    pivo = parameters['Pivô'].split(',')
    pivo = [int(ponto) for ponto in pivo]
    angulo = np.radians(int(parameters['Grau']))
    resultado = []
    for i in pontos:
        x, y = i

        rotacao_x = round(pivo[0] + (x - pivo[0]) * np.cos(angulo) - (y - pivo[1]) * np.sin(angulo))
        rotacao_y = round(pivo[1] + (x - pivo[0]) * np.sin(angulo) + (y - pivo[1]) * np.cos(angulo))

        resultado.append((rotacao_x, rotacao_y))

    return resultado