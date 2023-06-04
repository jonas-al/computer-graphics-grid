from grid.grid import Grid
from src.Bresenham import bresenham_algorithm
from src.Circunferencias import Circle
from src.CurvaBezier import Bezier
from src.Polilinha import polilinha
from src.PreencheVarre import PreenchePoligno
from src.RecorteLinha import recorte_linha
from src.Transforamacoes import rotacao
from src.Transforamacoes import translacao
from src.Transforamacoes import escala

grid = Grid(extent=10, size=500)

def my_render_cells_algorithm(selected_cells, rendered_cells, parameters):
    for cell in selected_cells:
        grid.render_cell(cell)

def render_cell(pontos):
    [grid.render_cell(cell) for cell in pontos]

def bresenham(selected_cells, rendered_cells, parameters):
    resultado = bresenham_algorithm(selected_cells, rendered_cells)
    render_cell(resultado)

def circunferencias(selected_cells, rendered_cells, parameters):
    resultado = Circle(selected_cells, rendered_cells)
    render_cell(resultado)

def curvas(selected_cells, rendered_cells, parameters):
    resultado = Bezier(selected_cells, rendered_cells)
    render_cell(resultado)

def polilinha_(selected_cells, rendered_cells, parameters):
    resultado = polilinha(selected_cells)
    render_cell(resultado)

def preenche_poligno(selected_cells, rendered_cells, parameters):
    resultado = PreenchePoligno(selected_cells, rendered_cells)
    render_cell(resultado)

def recorte_linha_(selected_cells, rendered_cells, parameters):
    resultado = recorte_linha(selected_cells, rendered_cells)
    grid._clear_all()
    render_cell(resultado)

def recorte_poligono(selected_cells, rendered_cells, parameters):
    x_minimo = int(parameters['X Mínimo'])
    y_minimo = int(parameters['Y Mínimo'])
    x_maximo = int(parameters['X Máximo'])
    y_maximo = int(parameters['Y Máximo'])
    grid.clip_window = [(x_minimo, y_minimo), (x_maximo, y_minimo), (x_maximo, y_maximo), (x_minimo, y_maximo)]
    grid._redraw()

def rotacao_(selected_cells, rendered_cells, parameters):
    resultado = rotacao(rendered_cells, parameters)
    grid._clear_all()
    render_cell(resultado)

def translacao_(selected_cells, rendered_cells, parameters):
    resultado = translacao(rendered_cells, parameters)
    grid._clear_all()
    render_cell(resultado)

def escala_(selected_cells, rendered_cells, parameters):
    resultado = escala(selected_cells, parameters)
    render_cell(resultado)

grid.add_algorithm(name="Renderiza Células:", parameters=None, algorithm=my_render_cells_algorithm)
grid.add_algorithm(name="Bresenham:", parameters=None, algorithm=bresenham)
grid.add_algorithm(name="Circunferência:", parameters=None, algorithm=circunferencias)
grid.add_algorithm(name="Curva", parameters=None, algorithm=curvas)
grid.add_algorithm(name="Polilinha:", parameters=None, algorithm=polilinha_)
grid.add_algorithm(name="Preenchimento:", parameters=None, algorithm=preenche_poligno)
grid.add_algorithm('Recorte de Linha', parameters=None, algorithm=recorte_linha_)
grid.add_algorithm(name='Recorte Poligono', parameters=['X Mínimo', 'Y Mínimo', 'X Máximo', 'Y Máximo'], algorithm=recorte_poligono)
grid.add_algorithm(name="Rotação:", parameters=['Grau', 'Pivô'], algorithm=rotacao_)
grid.add_algorithm(name="Translação:", parameters=['Ponto de Deslocamento'], algorithm=translacao_)
grid.add_algorithm(name="Escala:", parameters=['Ponto Fixo', 'Fator X', 'Fator Y'], algorithm=escala_)
grid.show()