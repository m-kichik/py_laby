from plot_maker import PlotMaker, str_div

# КАТОД

# Свет, напряжение на катоде

x_l_row = '''
0
0,99
1,48
1,98
2,49
2,98
3,51
3,99
'''
x_l = str_div(x_l_row)

y_cath_l_row = '''
0,03
0,04
0,05
0,05
0,05
0,06
0,06
0,07
'''
y_mkp_l_low = '''
8,85
8,85
8,85
8,85
8,86
8,86
8,87
8,87
'''
y_scr_l_row = '''
0,03
0,03
0,04
0,05
0,11
0,15
0,19
0,21
'''
y_an_l_row = '''
4,47
4,48
4,47
4,48
4,51
4,54
4,57
4,59
'''

y_cath_l = str_div(y_cath_l_row)
y_mkp_l = str_div(y_mkp_l_low)
y_scr_l = str_div(y_scr_l_row)
y_an_l = str_div(y_an_l_row)

# Без света, катод

x_d_row = '''
-0,01
1
1,5
1,99
2,5
2,99
3,5
4
4,24
'''
x_d = str_div(x_d_row)

y_cath_d_row = '''
0,02
0,03
0,03
0,04
0,04
0,05
0,05
0,05
0,06
'''
y_mkp_d_low = '''
8,98
8,96
8,98
8,96
8,98
8,98
8,99
8,98
9
'''
y_scr_d_row = '''
0,02
0,03
0,03
0,03
0,02
0,03
0,03
0,03
0,03
'''
y_an_d_row = '''
4,53
4,53
4,53
4,53
4,53
4,51
4,54
4,54
4,53
'''

y_cath_d = str_div(y_cath_d_row)
y_mkp_d = str_div(y_mkp_d_low)
y_scr_d = str_div(y_scr_d_row)
y_an_d = str_div(y_an_d_row)

plt_cath_1 = PlotMaker('ВАХ катода', 'U катода, кВ', 'I катода, мкА',
          [[x_l, y_cath_l], [x_d, y_cath_d]],
          True, False, None,
          'cath_cath', ['-', '--'], None)

plt_cath_1.make_plot()

plt_cath_2 = PlotMaker('ВАХ МКП', 'U катода, кВ', 'I МКП, мкА',
          [[x_l, y_mkp_l], [x_d, y_mkp_d]],
          True, False, None,
          'cath_mkp', ['-', '--'], None)

plt_cath_2.make_plot()

plt_cath_3 = PlotMaker('ВАХ экрана', 'U катода, кВ', 'I экрана, мкВ',
          [[x_l, y_scr_l], [x_d, y_scr_d]],
          True, False, None,
          'cath_scr', ['-', '--'], None)

plt_cath_3.make_plot()

plt_cath_4 = PlotMaker('ВАХ анода', 'U катода, кВ', 'I анода, мкВ',
          [[x_l, y_an_l], [x_d, y_an_d]],
          True, False, None,
          'cath_an', ['-', '--'], None)

plt_cath_4.make_plot()

# МКП

# Свет, напряжение на МКП

x_l_row = '''
0
0,032
0,5
0,8
1,1
1,4
1,71
2
'''
x_l = str_div(x_l_row)

y_cath_l_row = '''
0,03
0,04
0,04
0,05
0,05
0,05
0,05
0,06
'''
y_mkp_l_low = '''
0
1,34
2,1
3,35
4,66
6
7,46
8,9
'''
y_scr_l_row = '''
0,03
0,03
0,04
0,04
0,03
0,04
0,05
0,17
'''
y_an_l_row = '''
-0,01
1,065
1,06
1,68
2,35
3,03
3,8
4,59
'''

y_cath_l = str_div(y_cath_l_row)
y_mkp_l = str_div(y_mkp_l_low)
y_scr_l = str_div(y_scr_l_row)
y_an_l = str_div(y_an_l_row)

# Без света, напряжение на МКП

x_d_row = '''
0
0,32
0,61
0,9
1,2
1,5
1,8
2
'''
x_d = str_div(x_d_row)

y_cath_d_row = '''
0,03
0,02
0,04
0,04
0,04
0,05
0,04
0,05
'''
y_mkp_d_low = '''
0,01
1,33
2,57
3,82
5,13
6,48
7,96
8,94
'''
y_scr_d_row = '''
0,03
0,04
0,03
0,04
0,04
0,03
0,03
0,03
'''
y_an_d_row = '''
-0,01
0,66
1,28
1,92
2,58
3,27
4,03
4,52
'''

y_cath_d = str_div(y_cath_d_row)
y_mkp_d = str_div(y_mkp_d_low)
y_scr_d = str_div(y_scr_d_row)
y_an_d = str_div(y_an_d_row)

plt_mkp_1 = PlotMaker('ВАХ катода', 'U МКП, кВ', 'I катода, мкА',
          [[x_l, y_cath_l], [x_d, y_cath_d]],
          True, False, None,
          'mkp_cath', ['-', '--'], None)

plt_mkp_1.make_plot()

plt_mkp_2 = PlotMaker('ВАХ МКП', 'U МКП, кВ', 'I МКП, мкА',
          [[x_l, y_mkp_l], [x_d, y_mkp_d]],
          True, False, None,
          'mkp_mkp', ['-', '--'], None)

plt_mkp_2.make_plot()

plt_mkp_3 = PlotMaker('ВАХ экрана', 'U МКП, кВ', 'I экрана, мкА',
          [[x_l, y_scr_l], [x_d, y_scr_d]],
          True, False, None,
          'mkp_scr', ['-', '--'], None)

plt_mkp_3.make_plot()

plt_mkp_4 = PlotMaker('ВАХ анода', 'U МКП, кВ', 'I анода, мкА',
          [[x_l, y_an_l], [x_d, y_an_d]],
          True, False, None,
          'mkp_an', ['-', '--'], None)

plt_mkp_4.make_plot()

# ЭКРАН

# Свет, U экрана

x_l_row = '''
0,01
0,98
1,51
2
2,49
2,99
3,5
3,82
'''
x_l = str_div(x_l_row)

y_cath_l_row = '''
0,04
0,04
0,05
0,05
0,05
0,05
0,05
0,05
'''
y_mkp_l_low = '''
9,05
8,98
8,98
8,95
8,96
8,96
8,96
8,98
'''
y_scr_l_row = '''
0
0,12
0,13
0,14
0,15
0,16
0,16
0,17
'''
y_an_l_row = '''
4,55
4,6
4,59
4,6
4,6
4,6
4,6
4,6
'''

y_cath_l = str_div(y_cath_l_row)
y_mkp_l = str_div(y_mkp_l_low)
y_scr_l = str_div(y_scr_l_row)
y_an_l = str_div(y_an_l_row)

plt_scr_1 = PlotMaker('ВАХ катода', 'U экрана, кВ', 'I катода, мкА',
          [[x_l, y_cath_l]],
          True, False, None,
          'scr_cath')

plt_scr_1.make_plot()

plt_scr_2 = PlotMaker('ВАХ МКП', 'U экрана, кВ', 'I МКП, мкА',
          [[x_l, y_mkp_l]],
          True, False, None,
          'scr_mkp')

plt_scr_2.make_plot()

plt_scr_3 = PlotMaker('ВАХ экрана', 'U экрана, кВ', 'I экрана, мкА',
          [[x_l, y_scr_l]],
          True, False, None,
          'scr_scr')

plt_scr_3.make_plot()

plt_scr_4 = PlotMaker('ВАХ анода', 'U экрана, кВ', 'I анода, мкА',
          [[x_l, y_an_l]],
          True, False, None,
          'scr_an')

plt_scr_4.make_plot()

# Исследуем пределы видимости изображения

x_row = '''
1,55
1,7
2,08
2,39
2,69
2,98
3,27
3,58
3,89
4,24
'''
x = str_div(x_row)

y_row = '''
2
1,86
1,59
1,48
1,38
1,32
1,31
1,28
1,26
1,27
'''
y = str_div(y_row)

plt = PlotMaker('Зависимость минимального U МКП от U катода',
                'U катода, кВ', 'U МКП, мкА',
                [[x, y]], True, False, None,
                'min_mkp_cath')

plt.make_plot()
