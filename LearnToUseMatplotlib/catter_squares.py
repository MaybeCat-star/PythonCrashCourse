from matplotlib import pyplot

x_values = range(1, 1001)
y_values = [_ ** 2 for _ in x_values]


pyplot.style.use('seaborn')
fig, ax = pyplot.subplots()

ax.scatter(x_values, y_values, c = y_values, cmap = pyplot.cm.Greens, s = 10)

ax.set_title("squares", fontsize = 24)
ax.set_xlabel("value", fontsize = 14)
ax.set_ylabel("value squared", fontsize = 14)

ax.tick_params(axis = "both",which = 'major', labelsize = 14)

ax.axis([0, 1100, 0, 1100000])

# pyplot.savefig('square_plot.png', bbox_inches = 'tight')
pyplot.savefig('square_plot.png')
