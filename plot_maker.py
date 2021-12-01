from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


def polinom(x, coeffs):
    res = 0.
    deg = len(coeffs) - 1
    for c in coeffs:
        res += c * (x ** deg)
        deg -= 1
    return res


def poly_eq(coeffs):
    i = len(coeffs) - 1
    res = ''
    for c in coeffs:
        sign = ' -' if c < 0 else '+' if c > 0 else ''
        if i != 0:
            res += f'{sign} {abs(c):.3e} {f"x^{i}"}\n'#.format(sign, abs(c), f'x^{i}\n')
        else:
            res += f'{sign} {abs(c):.3e}'#.format(sign, abs(c))
        i -= 1
    res += ' = 0'
    return res


def appr_acc_poly(x, y, poly, coeffs):
    res = 0.
    for i in range(len(x)):
        res += (y[i] - poly(x[i], coeffs)) ** 2
    res /= len(x) * (len(x) - 1)
    res = res ** 0.5
    return res


def str_div(stroka):
    return [float(x) for x in stroka.replace(',', '.').split()]


class PlotMaker:

    def __init__(self, title, x_l, y_l, data,
                 connect_dots=False,
                 file_name='plot',
                 line_style_lib=None, marker_lib=None, color_lib=None):
        if marker_lib is None:
            marker_lib = ['o']
        self.title = title
        self.x_label = x_l
        self.y_label = y_l
        self.data = data
        self.c_dots = connect_dots
        self.file_name = file_name
        self.ls_lib = line_style_lib
        self.marker_lib = marker_lib
        self.color_lib = color_lib
        self.plot = plt

    def prepare_poly(self, d, deg):
        poly_coeffs = np.polyfit(d[0], d[1], deg)
        delta = (max(d[0]) - min(d[0])) / 100.
        if delta < 0.004:
            delta = 0.00004
        xnew = np.arange(min(d[0]), max(d[0]), delta)  # 280., 580., delta)
        return xnew, poly_coeffs

    def start(self):
        fig = plt.gcf()
        fig.set_size_inches(10, 8)
        plt.title(self.title, fontsize=16, fontweight="bold")
        plt.xlabel(self.x_label, fontsize=16)
        plt.ylabel(self.y_label, fontsize=16)
        plt.grid(True)

        counter = 0
        for d in self.data:
            # if len(d) == 2:
            #     err = [None, None]
            # else:
            #     err = d[2]
            err = [None, None]
            plt.errorbar(d[0], d[1], xerr=err[0], yerr=err[1], fmt=self.marker_lib[counter], color=self.color_lib[counter],
                         ecolor='black')

            if self.c_dots:
                if self.ls_lib != None:
                    ls = self.ls_lib[counter]
                else:
                    ls = '--'
                plt.plot(d[0], d[1], ls=ls, lw=2.5, color=self.color_lib[counter], label=d[2])

            counter += 1

    def add_appr(self, data_num=0, poly_degree=1, print_poly=False, print_max=False, custom_coeffs = None):
        xnew, poly_coeffs = self.prepare_poly(self.data[data_num], poly_degree)
        ynew = polinom(xnew, poly_coeffs)
        plt.plot(xnew, ynew, '--', lw=2.5,
                 color='darkgrey')  # , marker=self.marker_lib[counter])

        if print_poly:
            if custom_coeffs != None:
                poly_coeffs = custom_coeffs
            polyy_eq = np.poly1d(poly_coeffs)
            plt.legend([poly_eq(polyy_eq.coeffs)], loc='best', fontsize=14)
#            plt.legend([poly_eq], loc='best', fontsize=14)

        if print_max:
            x_max = xnew[np.where(ynew == max(ynew))]
            y_max = max(polinom(xnew, poly_coeffs))
            plt.scatter(x_max, y_max, marker='x', color='black', s=200)
            plt.legend([f'x_max = {round(x_max[0], 3)}, y_max = {round(y_max, 3)}'], loc=3, fontsize=14)

        return poly_coeffs

    def make_plot(self):
        plt.savefig(self.file_name)
        plt.clf()
        # plot = Image.open(self.file_name + '.png')
        # rgb_plot = plot.convert('RGB')
        # rgb_plot.save(self.file_name + '.jpg', 'JPEG')

