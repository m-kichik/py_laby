from plot_maker import PlotMaker

x = [1, 2, 3, 4, 5, 6]
y = [94761, 71535, 50035, 41606, 80295, 38553]

plt_1 = PlotMaker('Зависимость времени выполнения от количества процессов', 'количество процессов ед.', 'время, мс',
                  [[x, y]], False, 'kit_1')
plt_1.start()
plt_1.make_plot()

x_new = x[0:len(x) - 1]
y_new = [y[0] / el for el in y[1:len(y)]]

plt_2 = PlotMaker('Зависимость ускорения от количества процессов', 'количество процессов, ед.', 'ускорение, раз',
                  [[x_new, y_new]], False, 'kit_2')
plt_2.start()
plt_2.make_plot()