from plot_maker import str_div, PlotMaker

x_row_1 = '''
14,14
13,15
12,26
11,22
10,45
9,67
8,47
7,83
7,08
6,7
6,4
6,07
5,55
5,19
4,89
4,3
4,08
3,83
3,55
'''
x_row_2 = '''
-14,84
-13,79
-13
-11,97
-10,73
-9,9
-8,87
-7,94
-7,16
-6,93
-6,36
-5,95
-5,35
-5,11
-4,81
-4,34
-3,99
-3,59
-3,37
'''
x_1 = str_div(x_row_1)
x_2 = str_div(x_row_2)
x_2.reverse()

y_row_1 = '''
2225
2060
1882
1718
1578
1425
1165
1034
890
776
706
650
633
577
489
343
320
237
197
'''
y_row_2 = '''
-2371
-2175
-2041
-1881
-1666
-1492
-1306
-1163
-991
-946
-837
-752
-625
-601
-522
-388
-320
-205
-156
'''
y_1 = str_div(y_row_1)
y_2 = str_div(y_row_2)
y_2.reverse()

plt_1 = PlotMaker('Характеристика лазерного гироскопа при Iн = -1,3 мА',
                  'I, мА', 'Δν, Гц',
                  [[x_1, y_1], [x_2, y_2]], False, False,
                  file_name='1_3')

plt_1.make_plot()


x_row_1 = '''
14,12
13,05
12,76
11,13
10,14
9,39
8,33
7,82
7,35
6,87
6,33
5,96
5,71
5,17
5,01
4,81
4,56
4,33
4,03
3,91
3,77
'''
x_row_2 = '''
-14,8
-13,78
-12,85
-11,29
-10,5
-9,96
-9
-8,2
-7,28
-6,92
-6,17
-5,82
-5,27
-4,86
-4,35
-3,64
-3,98
-4,14
-4,38
-3,74
-3,22
-3,01
'''
x_1 = str_div(x_row_1)
x_2 = str_div(x_row_2)
x_2.reverse()

y_row_1 = '''
2269
2057
2013
1727
1523
1401
1191
1091
965
863
743
660
632
470
433
395
330
279
163
194
156
'''
y_row_2 = '''
-2380
-2182
-2014
-1738
-1617
-1499
-1321
-1173
-1035
-966
-800
-742
-656
-566
-459
-320
-407
-451
-520
-362
-205
-148
'''
y_1 = str_div(y_row_1)
y_2 = str_div(y_row_2)
y_2.reverse()

plt_2 = PlotMaker('Характеристика лазерного гироскопа при Iн = -1,4 мА',
                  'I, мА', 'Δν, Гц',
                  [[x_1, y_1], [x_2, y_2]], False, False,
                  file_name='1_4')

plt_2.make_plot()


x_row_1 = '''
14,19
13,2
12,16
11,25
10,28
9,12
8,5
7,68
7,08
6,48
5,7
5,42
5,07
4,89
4,73
4,62
'''
x_row_2 = '''
-14,91
-14
-12,68
-11,69
-10,35
-9,14
-8,34
-7,38
-6,3
-5,58
-5,16
-5,06
-5
-4,76
-4,51
-4,33
-4,13
-3,87
-3,52
-3,4
-3,14
-2,94
'''
x_1 = str_div(x_row_1)
x_2 = str_div(x_row_2)
x_2.reverse()

y_row_1 = '''
1600
1512
1361
1266
1137
982
873
770
645
566
390
359
254
216
204
193
'''
y_row_2 = '''
-1791
-1660
-1474
-1302
-1104
-943
-816
-653
-433
-290
-206
-212
-271
-238
-203
-205
-196
-170
-137
-145
-118
-105
'''
y_1 = str_div(y_row_1)
y_2 = str_div(y_row_2)
y_2.reverse()

plt_3 = PlotMaker('Характеристика лазерного гироскопа при Iн = -1,5 мА',
                  'I, мА', 'Δν, Гц',
                  [[x_1, y_1], [x_2, y_2]], False, False,
                  file_name='1_5')

plt_3.make_plot()


x_row_1 = '''
14,25
13,32
11,39
10,66
10,03
9,07
7,89
6,95
5,79
5,95
5,5
5,23
5,04
4,9
4,67
4,53
4,23
4,18
4,09
'''
x_row_2 = '''
-14,89
-13,61
-12,5
-11,2
-9,68
-8,6
-7,42
-6,75
-5,98
-5,52
-5,25
-5,07
-4,91
-4,76
-4,55
-4,27
-4,11
-3,98
-3,64
-3,36
'''
x_1 = str_div(x_row_1)
x_2 = str_div(x_row_2)
x_2.reverse()

y_row_1 = '''
1719
1589
1319
1187
1090
966
763
639
421
482
434
393
331
328
287
230
161
122
119
'''
y_row_2 = '''
-1803
-1643
-1487
-1294
-1044
-864
-695
-565
-405
-348
-299
-269
-277
-243
-243
-180
-191
-180
-139
-117
'''
y_1 = str_div(y_row_1)
y_2 = str_div(y_row_2)
y_2.reverse()

plt_4 = PlotMaker('Характеристика лазерного гироскопа при Iн = -1,6 мА',
                  'I, мА', 'Δν, Гц',
                  [[x_1, y_1], [x_2, y_2]], False, False,
                  file_name='1_6')

plt_4.make_plot()


x_row_1 = '''
-14,91
-13,77
-12,84
-11,54
-10,11
-9,15
-8,11
-7,05
-6,36
-5,75
-5,3
-5,04
-4,88
-4,55
-4,43
4,8
4,89
5,21
5,39
5,7
5,86
6,1
6,32
7,06
7,94
9,03
10,1
10,82
11,85
13,37
14,12
14,2
'''
x_row_2 = '''
14,2
14,23
13,35
12,66
10,97
9,79
8,53
7,39
6,92
6,14
5,77
5,38
4,98
4,73
4,57
4,47
4,33
4,09
3,97
3,92
3,78
3,71
3,54
3,49
3,38
3,32
3,26
3,17
3,14
-5,22
-5,33
-5,56
-6
-6,61
-7,66
-9,11
-10,08
-11,3
-12,64
-13,82
-14,9
'''
x_1 = str_div(x_row_1)
x_2 = str_div(x_row_2)
x_2.reverse()

y_row_1 = '''
-1820
-1672
-1558
-1360
-1135
-1001
-848
-676
-549
-417
-328
-277
-248
-183
-156
149
216
274
325
378
410
486
519
661
789
949
1137
1212
1387
1590
1675
1714
'''
y_row_2 = '''
1714
1700
1601
1505
1267
1121
922
760
705
576
504
422
371
326
285
263
259
210
194
190
162
164
129
110
105
89
67
63
67
-347
-400
-440
-560
-655
-850
-1068
-1200
-1380
-1575
-1748
-1872
'''
y_1 = str_div(y_row_1)
y_2 = str_div(y_row_2)
y_2.reverse()

plt_5 = PlotMaker('Характеристика лазерного гироскопа при Iн = -1,7 мА',
                  'I, мА', 'Δν, Гц',
                  [[x_1, y_1], [x_2, y_2]], False, False,
                  file_name='1_7', color_lib=['black', 'red'])

plt_5.make_plot()


x_row_1 = '''
14,24
13,47
12,09
11,23
10,33
9,03
7,81
6,62
5,55
4,84
4,17
3,98
3,84
3,7
3,33
3,18
3
2,74
2,66
2,45
2,28
2,2
2,16
2,12
1,99
1,91
1,81
1,71
'''
x_row_2 = '''
-14,91
-13,46
-12,99
-11,37
-10,16
-9,19
-8,1
-7,35
-6,84
-6,3
-5,39
-5,17
-5,06
-4,81
-4,64
-4,33
-4,13
-4,03
-3,94
-3,78
-3,58
'''
x_1 = str_div(x_row_1)
x_2 = str_div(x_row_2)
x_2.reverse()

y_row_1 = '''
-2169
-2048
-1813
-1686
-1533
-1330
-1108
-904
-690
-571
-473
-431
-391
-390
-310
-301
-267
-205
-205
-189
-165
-157
-128
-122
-101
-91
-86
-63
'''
y_row_2 = '''
2299
2036
1941
1668
1452
1259
1055
909
810
668
477
444
401
380
335
283
242
231
240
223
185
'''
y_1 = str_div(y_row_1)
y_2 = str_div(y_row_2)
y_2.reverse()

plt_6 = PlotMaker('Характеристика лазерного гироскопа при Iн = -1,7 мА, соседняя мода',
                  'I, мА', 'Δν, Гц',
                  [[x_1, y_1], [x_2, y_2]], False, False,
                  file_name='1_7_sm')

plt_6.make_plot()