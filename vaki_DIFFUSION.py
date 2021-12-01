from plot_maker import str_div, PlotMaker
import math

x = str_div('''
0
1
2
5
10
20
30
40
50
100
150
''')
y = [el / 1000. for el in str_div('''
-88000
16500
91000
280000
420000
540000
543000
500000
500000
500000
500000
''')]

plt_1 = PlotMaker('ВАХ молекулярно-электронной ячейки', 'U, мВ', 'I, мкА',
                  [[x, y]], True, file_name='VAH')

plt_1.make_plot()

x = str_div('''
0,05
0,1
0,2
0,5
1
2
5
10
20
''')
y = str_div('''
0,66
0,8
0,9
0,78
0,64
0,54
0,4
0,3
0,26
''')

plt_2 = PlotMaker('АЧХ молекулярно-электронной ячейки', 'f, Гц', 'A/A0',
                  [[x, y]], True, file_name='ACHH')

plt_2.make_plot()

x_ln = [math.log(el) for el in x]
y_ln = [math.log(el) for el in y]

plt_3 = PlotMaker('АЧХ молекулярно-электронной ячейки в логарифмических осях', 'ln(f)', 'ln(A/A0)',
                  [[x_ln, y_ln]], True, file_name='ACHH_LN')

plt_3.make_plot()