from bokeh.plotting import figure 
from bokeh.io import output_file, save, show
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d

x = [38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19]    
y = [28.9, 30.3, 25.0, 25.3, 27.4, 27.5, 26.4, 25.3, 25.3, 27.1, 26.8, 27.1, 26.7, 29.7, 28.4, 30.0, 27.3, 31.4, 27.2, 20.9]
    
output_file("grafico.html") #vai ser o nome com o qual o arquivo será salvo

figure = figure()
figure.line(x, y, color = "DarkRed")

figure.width = 1280
figure.height= 720
figure.background_fill_color = (255, 255, 255, 0.1)

figure.title.text = "Correlação Idade X Pontuação LeBron James"
figure.title.text_color = "Black"    
figure.title.text_font = "times"
figure.title.text_font_size = "30px"
figure.title.align = "center"

figure.xaxis.axis_label = "Idade" 
figure.xaxis.minor_tick_line_color = "black"
figure.xaxis.major_tick_line_color = "black"
figure.xaxis.minor_tick_in = 10
figure.xaxis.major_tick_in = 15

figure.yaxis.axis_label = "Pontuacão Por Jogo" 
figure.yaxis.minor_tick_line_color = "black"
figure.yaxis.major_tick_line_color = "black"
figure.yaxis.minor_tick_in = 10
figure.yaxis.major_tick_in = 15

figure.x_range = Range1d(start = 18, end = 40)
figure.y_range = Range1d(start = 20, end = 35)

figure.xgrid.grid_line_color = "black"
figure.xgrid.grid_line_alpha = 0.05
figure.ygrid.grid_line_color = "black"
figure.ygrid.grid_line_alpha = 0.05
figure.grid.grid_line_dash = "dashdot"

figure.xaxis[0].ticker.desired_num_ticks = 20
figure.yaxis[0].ticker.desired_num_ticks = 15
figure.xaxis[0].ticker.num_minor_ticks = 0
figure.yaxis[0].ticker.num_minor_ticks = 0

figure.axis.axis_label_text_color = "black"
figure.axis.axis_label_text_font = "times"
figure.axis.axis_label_text_font_size = "20px"


show(figure)
save(figure)