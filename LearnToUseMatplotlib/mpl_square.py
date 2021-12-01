from matplotlib import pyplot


squares = [_ ** 2 for _ in range(1, 6)]

print(squares)
fig, ax = pyplot.subplots()
ax.plot(squares)

pyplot.show()
