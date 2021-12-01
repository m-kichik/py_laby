from plot_maker import PlotMaker, str_div

x_cw = str_div('''
7,6
8,4
9,1
9,9
10,7
11,4
12,2
13
13,7
14,2
14,4
14,5
14,6
14,7
14,9
15
15,3
15,6
15,9
16,1
16,3
16,5
16,7
''')
y_cw = str_div('''
1
1
1
1
1
1
2
2
2
2
14
29
45
64
94
116
188
274
374
465
547
627
702
''')

x_q = str_div('''
7,6
8,5
9,4
10
11
12
13
14
14,5
15
15,4
15,7
16
16,2
16,4
16,6
16,7
''')
y_q = str_div('''1
1
1
1
1
2
2
2
28
115
217
287
376
461
538
607
639''')

plt = PlotMaker('зависимость V от I', 'I', 'V',
                [[x_cw, y_cw, 'cw'], [x_q, y_q, 'q']],
                connect_dots=True, file_name='gravirovka',
                marker_lib=['o', 'o'], color_lib=['green', 'orange'])
plt.start()
plt.make_plot()

x_imp = str_div('''
15,4
15,6
15,8
16
16,1
16,2
16,3
16,4
16,5
16,6
16,7
''')
y_imp = str_div('''
3,5
4
4,5
3
3
3
3,4
3,4
3,5
3,5
3,5
''')

plt_2 = PlotMaker('Зависимость полуширины импульса от I накачки', 'I', 'delta l',
                  [[x_imp, y_imp, '']], connect_dots=True,
                  file_name='gravirovka_2',
                  marker_lib=['o'], color_lib=['red'])
plt_2.start()
plt_2.make_plot()