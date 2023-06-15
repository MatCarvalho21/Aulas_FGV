from bokeh.plotting import figure 
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource

output_file("exemplo5.html")
raw_data = {"x": [1, 2, 3, 4, 5], "y":[2, 4, 6, 8, 10]} #NOSSOS DADOS BRUTOS

data_source = ColumnDataSource(data=raw_data) #FUNÇÃO QUE VAI CONVERTER OS DADOS

plot = figure()
#plot.circle(x ="x", y="y", source = data_source)

new_data = [3, 6, 9, 12, 15]

data_source.data["z"] = new_data
plot.circle(x ="x", y="z", source = data_source)

data_source.patch({"x":[(0, 10), (1, 20)], "z":[(0, 10), (1, 20)]}) #CADA TUPLA RECEBE O INDICE QUE DESEJO ALTERAR E O VALOR QUE QUEREMOS ADICIONAR 


show(plot)