from plot_maker import PlotMaker, str_div
import numpy as np
import math

x_neon = str_div('''
2594
2561
2544
2526
2450
2426
2415
2376
2366
2346
2334
2318
2298
2276
2268
2248
2236
2216
2192
2178
2148
2134
1871
1832
1824
''')
x_neon.reverse()
y_neon = str_div('''
7032
6929
6867
6828
6599
6533
6507
6402
6383
6334
6305
6267
6217
6164
6143
6096
6074
6030
5976
5945
5882
5852
5401
5341
5331
''')
y_neon.reverse()

plt_neon = PlotMaker(title='Зависимость λ от угла',
                     x_l='угол, градусы', y_l='λ, Å',
                     data=[[x_neon, y_neon]],
                     file_name='2_2_3_neon')
plt_neon.start()
neon_poly = np.poly1d(plt_neon.add_appr(poly_degree=4, print_poly=True))
plt_neon.make_plot()

print(f'neon_poly {neon_poly}')
neon_p_y = neon_poly(x_neon)
neon_p_y_av = sum(neon_p_y) / len(neon_p_y)
neon_err = math.sqrt(sum([(y - t_y) ** 2 for y, t_y in zip(neon_p_y, y_neon)]) / (len(neon_p_y) - 1)) / neon_p_y_av * 100
print(f'neon_err = {neon_err}')

x_hg = str_div('''
2550
2304
2100
2088
1908
1488
825
284
''')
x_hg.reverse()
y_hg = str_div('''
6907
6234
5791
5770
5461
4916
4358
4047
''')
y_hg.reverse()

plt_hg = PlotMaker(title='Зависимость λ от угла',
                   x_l='угол, градусы', y_l='λ, Å',
                   data=[[x_hg, y_hg]],
                   file_name='2_2_3_hg')
plt_hg.start()
hg_poly = np.poly1d(plt_hg.add_appr(poly_degree=4, print_poly=True))
plt_hg.make_plot()

print(f'hg_poly {hg_poly}')
hg_p_y = hg_poly(x_hg)
hg_p_y_av = sum(hg_p_y) / len(hg_p_y)
hg_err = math.sqrt(sum([(y - t_y) ** 2 for y, t_y in zip(hg_p_y, y_hg)]) / (len(hg_p_y) - 1)) / hg_p_y_av * 100
print(f'hgn_err = {hg_err}')


def find_lambda(x):
    if x >= 1824:
        return neon_poly(x)
    else:
        return hg_poly(x)


def k(m):
    return 1/4 - 1/(m ** 2)


x_h = [791., 1432., 2434]
lambda_h = [find_lambda(x) for x in x_h]
rg_h = []
for l, m in zip(lambda_h, [5, 4, 3]):
    rg_h.append(1e8 / (l * k(m)))
print(rg_h)
rg_av = sum(rg_h) / len(rg_h)
print(f'rg_av = {rg_av}')
print(f'rg_err = {math.sqrt(sum([(rg_av - x) ** 2 for x in rg_h]) / (len(rg_h) - 1))}')

x_i = [1690., 2183., 2295]
lambda_i = [find_lambda(x) for x in x_i]