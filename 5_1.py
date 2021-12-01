from plot_maker import PlotMaker, str_div

x_al_row = '''
2,00
4,00
6,00
8,00
10,00
'''
x_al = str_div(x_al_row)
y_al_row = '''
0,46
0,87
1,29
1,70
2,11
'''
y_al = str_div(y_al_row)

plt_al = PlotMaker(
    'Зависимость ln(N0/N) от l для алюминия', 'l, см', 'ln(N0/N)',
    [[x_al, y_al, [[0.01, 0.01, 0.01, 0.01, 0.01], [0.014, 0.026, 0.039, 0.05, 0.063]]]], 1, 'al'
)
plt_al.make_plot()

x_fe_row = '''
0,99
2,00
3,00
4,00
5,00
'''
x_fe = str_div(x_fe_row)
y_fe_row = '''
0,62
1,20
1,77
2,32
2,89
'''
y_fe = str_div(y_fe_row)

plt_fe = PlotMaker(
    'Зависимость ln(N0/N) от l для железа', 'l, см', 'ln(N0/N)',
    [[x_fe, y_fe, [[0.01, 0.01, 0.01, 0.01, 0.01], [0.019, 0.036, 0.053, 0.07, 0.09]]]], 1, 'fe'
)
plt_fe.make_plot()

x_pb_row = '''
0,44
0,94
1,41
1,89
2,33
'''
x_pb = str_div(x_pb_row)
y_pb_row = '''
0,56
1,16
1,69
2,26
2,72
'''
y_pb = str_div(y_pb_row)

plt_pb = PlotMaker(
    'Зависимость ln(N0/N) от l для свинца', 'l, см', 'ln(N0/N)',
    [[x_pb, y_pb, [[0.01, 0.01, 0.01, 0.01, 0.01], [0.017, 0.035, 0.05, 0.068, 0.082]]]], 1, 'pb'
)
plt_pb.make_plot()