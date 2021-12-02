from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice


dice = Dice()
results = []
for roll_num in range(1000):
	result = dice.roll()
	results.append(result)

frequencies = []
for value in range(1, dice.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

x_values = list(range(1, dice.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'results'}
y_axis_config = {'title': 'frequencies'}
my_layout = Layout(title="Results of rolling one D6 1000 times",
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')
