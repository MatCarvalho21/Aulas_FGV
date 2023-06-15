from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
import numpy as np 
from sklearn import datasets
from bokeh.models import Range1d 

output_file("exemplo4.html")

plot = figure(width = 640, height = 480, tools = "box_zoom,pan,reset,save,wheel_zoom") 
plot2 = figure()

plot.toolbar.logo = None #VAI RETIRAR O LOGO DA FERRAMENTA DA VISUALIZAÇÃO
plot.toolbar.autohide = True #VAI OCULTAR A BARRA DE FERRAENTAS
plot.toolbar_location = "below" #VAI INSERIR A POSIÇÃO DA BARRA DE FERRAMENTAS 

renderer = plot.circle([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], legend_label="some label") #resolver o negócio da legenda
plot.legend.location = "top_left"
plot.legend.background_fill_alpha = 0
plot.legend.border_line_color = None
# plot.legend.padding = 42 #VAI CONFIGURAR O PREENCHIMENTO DA LEGENDA DOS DADOS 

plot.legend.label_text_color = "cyan"
plot.legend.label_text_font = "times"

glyph_render = renderer.glyph
glyph_render.size = 42
glyph_render.fill_alpha = 0.15
glyph_render.line_color = "gold"
glyph_render.line_width = 2
glyph_render.line_dash = [7, 3]

show(plot)

