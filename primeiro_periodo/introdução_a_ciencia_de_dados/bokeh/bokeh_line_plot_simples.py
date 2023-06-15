from bokeh.plotting import figure 
from bokeh.io import output_file, save, show

x = [1, 7, 13, 42]
y = [2, 14, 26, 84]

output_file("line_plot.html") #vai ser o nome com o qual o arquivo será salvo

figure = figure()

figure.line(x, y)
#figure.circle(x, y)
#figure.triangle(x, y)

#0save(figure)
show(figure) #vai automaticamente abrir o navegador com o html