from plot_maker import PlotMaker, str_div, polinom, appr_acc_poly
from scipy.optimize import minimize_scalar


def rev_poly(x, coeffs):
    return (-1) * polinom(x, coeffs)


# U1 = 2,56V

v_c_1_row = '''
-0,006
0,348
0,472
0,553
0,63
0,674
0,71
0,871
0,955
1,114
1,222
1,346
1,711
1,728
1,768
1,797
1,863
2,031
2,202
2,657
3,099
3,485
4,642
5,422
6,096
6,32
6,592
7,192
7,706
8,283
8,706
9,513
10,055
11,088
11,503
'''
v_c_1 = str_div(v_c_1_row)
i_a_1_row = '''
0,0008
0,0009
0,0012
0,002
0,0043
0,0071
0,0108
0,0702
0,1678
0,555
0,874
1,235
1,781
1,8
1,804
1,793
1,781
1,655
1,493
1,052
0,746
0,612
0,402
0,3344
0,311
0,299
0,307
0,317
0,315
0,337
0,364
0,425
0,527
0,644
0,722
'''
i_a_1 = str_div(i_a_1_row)

plt_1 = PlotMaker(
    'Зависимость Ia от Vк при напряжении накала 2,56В', 'Vк, В', 'Ia, мкА',
    [[v_c_1, i_a_1]], True, False, file_name='1_3_1'
)
plt_1.make_plot()

# MAX

v_1_max = v_c_1[12:17]
i_1_max = i_a_1[12:17]

plt_1_max = PlotMaker(
    'Зависимость Ia от Vк при напряжении накала 2,56В (MAX)', 'Vк, В', 'Ia, мкА',
    [[v_1_max, i_1_max]], False, True, 4,
    file_name='1_3_1_max'
)
plt_1_max.make_plot()

max_1 = minimize_scalar(rev_poly, bounds=(v_1_max[0], v_1_max[-1]), args=(plt_1_max.poly_coeffs[0],))
print(f'x_max_1  : {max_1.x}\n'
      f'f_max_1  : {(-1) * max_1.fun}\n'
      f'appr_acc : {appr_acc_poly(v_1_max, i_1_max, polinom, plt_1_max.poly_coeffs[0])}\n')

# MIN

v_1_min = v_c_1[22:31]
i_1_min = i_a_1[22:31]

plt_1_min = PlotMaker(
    'Зависимость Ia от Vк при напряжении накала 2,56В (MIN)', 'Vк, В', 'Ia, мкА',
    [[v_1_min, i_1_min]], False, True, 4,
    file_name='1_3_1_min'
)
plt_1_min.make_plot()

min_1 = minimize_scalar(polinom, bounds=(v_1_min[0], v_1_min[-1]), args=(plt_1_min.poly_coeffs[0],))
print(f'x_min_1  : {min_1.x}\n'
      f'f_min_1  : {min_1.fun}\n'
      f'appr_acc : {appr_acc_poly(v_1_min, i_1_min, polinom, plt_1_min.poly_coeffs[0])}\n')

# U2 = 2,32V

v_c_2_row = '''
0,006
0,28
1,034
1,288
1,356
1,447
1,68
1,703
1,707
1,802
1,882
2,128
2,368
2,556
2,812
3,016
3,383
3,505
3,823
4,399
4,512
4,805
4,881
5,13
5,205
5,476
5,64
5,908
6,196
6,538
7,12
7,63
8,089
8,443
8,842
9,4
9,77
10,25
11,66
'''
v_c_2_obr_row = '''
10,452
9,698
9,276
8,909
8,642
8,384
8
7,783
7,546
7,07
6,295
5,497
4,816
4,034
3,511
3,021
2,4
1,972
1,575
1,412
1,268
1,109
1,044
0,816
0,654
0,452
0,007
'''
v_c_2 = str_div(v_c_2_row)
v_c_2_obr = str_div(v_c_2_obr_row)
i_a_2_row = '''
0,00011
0,00699
0,1321
0,702
0,887
1,075
1,22
1,206
1,213
1,135
1,037
0,865
0,671
0,548
0,425
0,351
0,268
0,249
0,21
0,171
0,166
0,1545
0,1478
0,139
0,144
0,135
0,128
0,133
0,134
0,13
0,117
0,1175
0,124
0,131
0,143
0,137
0,162
0,185
0,236
'''
i_a_2_obr_row = '''
0,172
0,145
0,126
0,121
0,11
0,105
0,1
0,099
0,098
0,102
0,104
0,115
0,131
0,165
0,205
0,291
0,519
0,856
1,076
0,9111
0,584
0,217
0,121
0,008
0,0018
0,001
0,0009
'''
i_a_2 = str_div(i_a_2_row)
i_a_2_obr = str_div(i_a_2_obr_row)

plt_2 = PlotMaker(
    'Зависимость Ia от Vк при напряжении накала 2,32В', 'Vк, В', 'Ia, мкА',
    [[v_c_2, i_a_2], [v_c_2_obr, i_a_2_obr]], True, False, file_name='1_3_2',
    line_style_lib=['-', '--']
)
plt_2.make_plot()

# MAX

v_2_max = v_c_2[5:10]
i_2_max = i_a_2[5:10]

plt_2_max = PlotMaker(
    'Зависимость Ia от Vк при напряжении накала 2,32В (MAX)', 'Vк, В', 'Ia, мкА',
    [[v_2_max, i_2_max]], False, True, 2,
    file_name='1_3_2_max'
)
plt_2_max.make_plot()

max_2 = minimize_scalar(rev_poly, bounds=(v_2_max[0], v_2_max[-1]), args=(plt_2_max.poly_coeffs[0],))
print(f'x_max_2  : {max_2.x}\n'
      f'f_max_2  : {(-1) * max_2.fun}\n'
      f'appr_acc : {appr_acc_poly(v_2_max, i_2_max, polinom, plt_2_max.poly_coeffs[0])}\n')

# MIN

v_2_min = v_c_2[19:38]
i_2_min = i_a_2[19:38]

plt_2_min = PlotMaker(
    'Зависимость Ia от Vк при напряжении накала 2,32В (MIN)', 'Vк, В', 'Ia, мкА',
    [[v_2_min, i_2_min]], False, True, 4,
    file_name='1_3_2_min'
)
plt_2_min.make_plot()

min_2 = minimize_scalar(polinom, bounds=(v_2_min[0], v_2_min[-1]), args=(plt_2_min.poly_coeffs[0],))
print(f'x_min_2  : {min_2.x}\n'
      f'f_min_2  : {min_2.fun}\n'
      f'appr_acc : {appr_acc_poly(v_2_min, i_2_min, polinom, plt_2_min.poly_coeffs[0])}\n')
