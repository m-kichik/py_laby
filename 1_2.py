from plot_maker import str_div, PlotMaker
import math

y_row = str_div('''
991
954
819
754
707
643
565
494
432
393
362
336
264
''')
N_0 = y_row[0]
# y = [1 / el - 1 / N_0 for el in y_row]
y = [1 / el for el in y_row]

x = str_div('''
0,0000
0,0015
0,0060
0,1340
0,2330
0,3572
0,5000
0,6580
0,8260
1,0000
1,1730
1,3420
1,5000
''')

plt = PlotMaker('Зависимость 1/N(θ) от 1 - cosθ', '1 - cosθ', '1/N(θ)',
                [[x, y]], file_name='1_2_')
plt.start()
coeffs = plt.add_appr(print_poly=True)
plt.make_plot()

print(coeffs)

k = coeffs[0]
b = coeffs[1]


def err_x(x, y):
    return sum([x_ ** 2 for x_ in x]) / len(x) - (sum([(y_ - b) / k for y_ in y]) / len(x)) ** 2


def err_y(x, y):
    return (sum([1 / (y_ - (k * x_ + b)) ** 2 for x_, y_ in zip(x, y)]) / len(x))


sigma_y = err_y(x, y)
D_xx = err_x(x, y)
W = err_y(x, y)

sigma_k = math.sqrt(1 / (D_xx * W))
print(sigma_k)

sigma_b = sigma_k * math.sqrt(sum([x_ ** 2 for x_ in x]) / len(x))
print(sigma_b)
