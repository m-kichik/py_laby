from plot_maker import PlotMaker

def str_div(stroka):
    return [float(x) for x in stroka.replace(',', '.').split()]

x_4_row_up = '''
0,06
5,66
10,27
15,05
18,32
20,05
20,73
22,40
22,74
23,04
23,59
24,58
25,87
27,01
28,88
31,01
33,53
35,20
35,85
38,82
40,34
42,73
46,62
51,36
63,54
'''
x_4_row_down = '''
48,04
42,52
40,37
37,21
34,62
33,30
30,59
28,14
25,49
24,02
22,50
20,08
15,54
12,33
9,29
6,58
3,24
0,06
'''
x_4_up = str_div(x_4_row_up)
x_4_down = str_div(x_4_row_down)
y_4_row_up = '''
12,5
85
165
237,5
280
287,5
290
275
250
220
212,5
225
255
275
310
350
400
425
430
430
415
405
415
450
455
'''
y_4_row_down = '''
425
405
415
435
425
400
350
300
250
220
275
292,5
250
200
150
100
50
12,5
'''
y_4_up = str_div(y_4_row_up)
y_4_down = str_div(y_4_row_down)

plt_4 = PlotMaker(
    'Зависимость Iк от Uа, Uз = 4В', 'Iк, мкА', 'Uа, В',
    [[x_4_up, y_4_up],
     [x_4_down, y_4_down]
     ], '4v',
    ['o', 'x']
)
plt_4.make_plot()

x_6_row_up = '''
0,06
5,08
8,13
11,06
14,33
17,96
18,97
19,66
20,85
23,44
23,95
24,14
24,94
25,55
26,97
29,27
31,53
34,18
36,04
38,32
39,26
41,87
44,32
46,71
47,89
53,65
60,12
64,98
65,23
67,18
76,33
'''
x_6_row_down = '''
62,64
53,56
47,41
44,52
42,20
39,41
37,54
33,30
30,28
27,85
26,56
25,45
24,16
23,50
23,36
21,85
19,05
14,47
11,05
8,26
5,16
0,06
'''
x_6_up = str_div(x_6_row_up)
x_6_down = str_div(x_6_row_down)
y_6_row_up = '''
0
50
100
150
200
250
260
265
265
205
150
145
140
145
175
225
275
325
350
355
350
325
310
305
310
350
400
410
410
415
425
'''
y_6_row_down = '''
410
350
310
310
325
350
355
310
250
200
165
145
145
175
220
260
260
200
150
100
50
0
'''
y_6_up = str_div(y_6_row_up)
y_6_down = str_div(y_6_row_down)

plt_6 = PlotMaker(
    'Зависимость Iк от Uа, Uз = 6В', 'Iк, мкА', 'Uа, В',
    [[x_6_up, y_6_up],
     [x_6_down, y_6_down]
     ], '6v',
    ['o', 'x']
)
plt_6.make_plot()

x_8_row_up = '''
0,07
6,95
9,84
12,90
16,22
18,00
20,39
22,15
23,50
23,95
24,06
25,42
26,80
28,47
30,57
32,96
35,82
37,44
39,87
43,48
48,06
50,15
56,22
60,84
66,34
75,30
'''
x_8_row_down = '''
68,40
56,65
49,83
46,55
43,77
40,33
39,15
36,39
34,15
31,59
29,47
27,25
25,37
24,81
23,96
23,96
23,16
22,20
19,70
16,16
12,85
9,87
7,19
2,83
0,07
'''
x_8_up = str_div(x_8_row_up)
x_8_down = str_div(x_8_row_down)
y_8_row_up = '''
0
50
100
150
200
225
245
245
225
152,5
115
90
95
125
175
225
275
285
280
250
225
230
275
300
305
315
'''
y_8_row_down = '''
305
275
230
230
250
275
285
280
250
200
150
100
90
95
127,5
190
230
245
240
200
150
100
50
0
0
'''
y_8_up = str_div(y_8_row_up)
y_8_down = str_div(y_8_row_down)

plt_8 = PlotMaker(
    'Зависимость Iк от Uа, Uз = 8В', 'Iк, мкА', 'Uа, В',
    [[x_8_up, y_8_up],
     [x_8_down, y_8_down]
     ], '8v',
    ['o', 'x']
)
plt_8.make_plot()

plt_both = PlotMaker(
    'Зависимость Iк от Uа', 'Iк, мкА', 'Uа, В',
    [[x_4_up, y_4_up],
     [x_4_down, y_4_down],
     [x_6_up, y_6_up],
     [x_6_down, y_6_down],
     [x_8_up, y_8_up],
     [x_8_down, y_8_down]
     ], 'both',
    ['o', 'x', 's', 'x', 'v', 'x']
)
plt_both.make_plot()