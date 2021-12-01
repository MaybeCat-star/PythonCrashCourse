from matplotlib import pyplot

input_values = range(1, 6)
squares = [_ ** 2 for _ in input_values]


# for style in pyplot.style.available:
pyplot.style.use('classic')
# after I used all the style one by one, I find I like this one.	
fig, ax = pyplot.subplots()
ax.plot(input_values, squares, linewidth = 3)
ax.set_title("squares", fontsize = 24)
ax.set_xlabel("value", fontsize = 14)
ax.set_ylabel("value squared", fontsize = 14)
ax.tick_params(axis = "both", labelsize = 14)
# print(style)
pyplot.show()
