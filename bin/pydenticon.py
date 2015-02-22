#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Raúl Jornet Calomarde'
__contact__ = 'rjornetc@openmailbox.org'
__copyright__ = 'Copyright © 2015, Raúl Jornet Calomarde'
__license__ = '''License GPLv3+: GNU GPL version 3 or any later
This program isfree software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or any later version. This program
is distributed  in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE. See the GNU General Public License for more details.
<http://www.gnu.org/licenses/>'''
__date__ = '2015-02-19'
__version__ = '0.0'

import sys, getopt
import svgwrite
import pydenticoncolor


SYMMETRIC_PATH_LIST = (
            #(),                                                            #
            (
                (0, 0),        (1, 0),         (1, 1),         (0, 1)),    # ■
            (
                (0.5, 0),      (0.5, 1),       (0, 1),         (1, 0),     # ◢◢
                (1, 1),        (0.5, 1),       (1, 0.5),       (0, 0.5)),  # ◢◢
            (
                (0.5, 0),      (1, 0.5),       (0.5, 1),       (0, 0.5),   # ◇
                (0.5, 0),      (0.5, 0.25),    (0.75, 0.5),    (0.5, 0.75),
                (0.25, 0.5),   (0.5, 0.25)),
            (
                (0, 0),        (0.5, 0.25),    (0.75, 0.5),    (1, 0),     # ◤◥
                (0.5, 0.25),   (0.25, 0.5),    (0, 1),         (0.5, 0.75),# ◣◢
                (0.75, 0.5),   (1, 1),         (0.5, 0.75),    (0.25,0.5)),
            (
                (0, 0),        (1, 0),         (0, 1)),                    # ◩
            (
                (0.5, 0),      (1, 0.5),       (0.5, 1),       (0.5, 0)))  # ◆

ASYMMETRIC_PATH_LIST = (
            (   
                (0, 0),        (1, 0),         (1, 0.5),       (0, 0.5)),  # ⬒
            (
                (0, 0),        (1, 0),         (0, 0.5),       (1, 0.5),   # ■◤
                (0, 1)),                                                   # ■◤
            (
                (0, 0),        (1, 0),         (0, 0.5),       (0.5, 0.5), # ■◤
                (0, 1)),                                                   # ◤
            (
                (0, 0),        (0.5, 0),       (1, 0.5),       (0.5, 1),   # ◥◣
                (0, 1),        (0.5, 0.5)),                                # ◢◤
            (
                (0, 0),        (1, 0.5),       (0, 1)),                    # ▶
            (
                (0, 0),        (1, 0.5),       (0, 1),         (0.5, 0.5)),# >
            (
                (0.5, 0),      (1, 0),         (0.5, 1),       (0, 1)),    # /
            (
                (0, 0),        (1, 0),         (1, 1),         (0.75, 0.5),#
                (0.25,0.5),    (0.5, 1),       (0.75, 0.5),    (0.5, 0),   #
                (0, 1)))

def rotate_path(path, rotation):
    if rotation in (90, 180, 270):
        pass
        #TODO
    else:
        raise(ValueError('The rotation must be a quarter in degrees'))

class Identicon():
    string = ''
    plots_number = 0
    plot_depth = 0
    symmetric_plots = []
    asymmetric_plots = []
    colors = []
    matrix_size = 0
    sub_matrix_size = 0
    size = 0
    
    
    def __init__(self,
                 hash,
                 matrix_size = 4,
                 size = 128,
                 number_of_colors = 1,
                 only_symmetric_diagonals = False):
        if size % 2 != 0:
            raise(ValueError('Size must be pair'))
          
        if size % matrix_size != 0:
            raise(ValueError('Size must be divisible by matrix_size'))
            #print('size must be divisible by matrix_size')
      
        try:
            self.string = hash.hexdigest()
        except AttributeError:
            if isinstance(hash, str):
                self.string = hash
            else:
                raise(ValueError('The hash must be a hash or string object'))
        
        self.matrix_size = matrix_size
        self.sub_matrix_size = int(0.5 + self.matrix_size / 2.0)
        self.colors = pydenticoncolor._get_string_color(self.string, min(number_of_colors, self.sub_matrix_size))
        self.size = size
        self.plots_number = self.sub_matrix_size
        for i in range(0, self.sub_matrix_size):
            self.plots_number += i
        self.plot_depth = len(self.string) / self.plots_number
        
        self._set_symmetric_plots(only_symmetric_diagonals)
        self._set_asymmetric_plots()
    
    
    def get_svg(self, filename):
        svg = svgwrite.Drawing(filename = filename,
                               size=(str(self.size) + 'px',
                                     str(self.size) + 'px'),
                               profile='tiny')
        plot_size = self.size / self.matrix_size
        
        asymmetric_count = -1
        
        sym_eighth_g = svg.defs.add(svg.g(id='sym'))
        asy_eighth_g = svg.defs.add(svg.g(id='asy'))
        
        for x in range(0, self.sub_matrix_size):
            for y in range(x, self.sub_matrix_size):
                if x == y:
                    sym_eighth_g.add(svg.polygon(
                                self._displace_path(
                                    self._scale_path(self.symmetric_plots[x], plot_size),
                                                     (x * plot_size,
                                                      y * plot_size)),
                                fill=self.colors[0]))
                else:
                    asymmetric_count += 1
                    asy_eighth_g.add(svg.polygon(
                                self._displace_path(
                                    self._scale_path(self.asymmetric_plots[asymmetric_count], plot_size),
                                                     (x * plot_size,
                                                      y * plot_size)),
                                fill=self.colors[min(abs(x - y),len(self.colors)-1)]))
        
        quarter_g = svg.defs.add(svg.g(id='quar'))
        quarter_g.add(svg.use(sym_eighth_g))
        quarter_g.add(svg.use(asy_eighth_g))
        asy_rot = svg.use(asy_eighth_g)
        plots_size = self.sub_matrix_size * plot_size
        
        asy_rot.rotate(90, center=(0, 0))
        asy_rot.scale(1,-1)
        #asy_rot.translate(0,-plots_size)
        quarter_g.add(asy_rot)
        
        #u = svg.use(quarter_g, insert = (0,0))
        #svg.add(u)
        
        for y in (0, 1):
            for x in (0, 1):
                u = svg.use(quarter_g)
                            #insert = (x * plots_size, y * plots_size))
                
                u.rotate(90 * abs(3 * x - y), (plots_size, plots_size))
                svg.add(u)
        return(svg)
    
    
    def _scale_path(self, path, multiplier):
        new_path = []
        for point in path:
            new_point = []
            for value in point:
                new_point.append(value * multiplier)
            new_path.append(tuple(new_point))
        return(tuple(new_path))
    
    
    def _displace_path(self, path, displacement):
        new_path = []
        for point in path:
            new_point = []
            for i in (0, 1):
                new_point.append(point[i] + displacement[i])
            new_path.append(tuple(new_point))
        return(tuple(new_path))
    
    
    def _set_symmetric_plots(self, only_symmetric):
        self.symmetric_plots = []
        for i in range(0, self.sub_matrix_size):
            if only_symmetric:
                self.symmetric_plots.append(
                    SYMMETRIC_PATH_LIST[int(self.string[self.plot_depth * i :
                                                        self.plot_depth * (i + 1)],
                                            16) % len(SYMMETRIC_PATH_LIST)])
            else:
                self.symmetric_plots.append(
                    (ASYMMETRIC_PATH_LIST+SYMMETRIC_PATH_LIST)[int(self.string[self.plot_depth * i :
                                                        self.plot_depth * (i + 1)],
                                            16) % len((ASYMMETRIC_PATH_LIST+SYMMETRIC_PATH_LIST))])
    
    
    def _set_asymmetric_plots(self):
        self.asymmetric_plots = []
        for i in range(0, self.plots_number - self.sub_matrix_size):
            self.asymmetric_plots.append(
                (ASYMMETRIC_PATH_LIST+SYMMETRIC_PATH_LIST)[int(self.string[self.sub_matrix_size +\
                                                    self.plot_depth * i :
                                                    self.sub_matrix_size +\
                                                    self.plot_depth * (i + 1)],
                                        16) % len(ASYMMETRIC_PATH_LIST+SYMMETRIC_PATH_LIST)])


if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:],'hv',['help','version'])
    except getopt.GetoptError:
        print('TODO')#TODO: Help string
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('TODO')#TODO: Help string
            sys.exit()
        elif opt in ('-v', '--version'):
            print ('TODO ' + __version__ + '\n' + __copyright__ + '\n' + __license__)#TODO: App name
            sys.exit()
