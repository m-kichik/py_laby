from plot_maker import str_div, PlotMaker
import numpy as np

x_row = '''
701,5
902,8
1593,5
1725
1805,4
'''
x = str_div(x_row)

y_row = '''
0,511
0,662
1,173
1,275
1,332
'''
y = str_div(y_row)
#y = [el * 1e6 for el in y]
#print(y)

plt = PlotMaker('Зависимость Е от номера канала N', 'N', 'E, МэВ',
                [[x, y]], True, True, 1, True, '5_5_calibrovochnii')
plt.make_plot()

x_row = '''
0,326
0,471
0,956
1,069
'''
x = str_div(x_row)

y_row = '''
0,341
0,478
0,956
1,069
'''
y = str_div(y_row)

plt_2 = PlotMaker('Зависимость Е рассчитанного от Е экспериментального', 'E, МэВ', 'E, МэВ',
                [[x, y]], False, True, 1, False, file_name='5_5_kompton')
plt_2.make_plot()

x_row = '''
0,750750751
0,784313725
0,852514919
1,510574018
1,956947162
14,04731134
27,86291446
'''
x = str_div(x_row)

y_row = '''
0,002738778
0,00229272
0,002834995
0,004116909
0,00525537
0,012838162
0,098220852
'''
y = str_div(y_row)
y = [el ** (0.5) for el in y]

plt_3 = PlotMaker('Зависимость R от 1/Е^(1/2)', '1/E^(1/2)', 'R',
                [[x, y]], False, True, 2, True, file_name='5_5_poly_approximation')
plt_3.make_plot()

x = [0.662, 1.173, 1.275]
xx = np.arange(0.400, 1.600, 0.1)
y = [0.207, 0.237, 0.195]
yy =  [e / (1 + 2 * e / 0.511) for e in xx]

plt_4 = PlotMaker('Зависимость E обратного рассеяния от Е фотопика', 'Eф, МэВ', 'Ео, МэВ',
                [[x, y], [xx, yy]], True, False, None, False, file_name='5_5_obr_rass', marker_lib=['o', 'o'], line_style_lib=['-', '--'])
plt_4.make_plot()

