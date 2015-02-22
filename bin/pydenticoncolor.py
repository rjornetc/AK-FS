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

import hashlib

def get_hash_color(hash, number_of_colors):
    string = hash.hexdigest()
    return(_get_string_color(string, number_of_colors))


def get_hexstring_color(hexstring, number_of_colors):
    int(hexstring, 16)
    return(_get_string_color(hexstring, number_of_colors))


def _get_string_color(string, number_of_colors):
    if len(string) / 6 >= number_of_colors:
        division_length = len(string) / (6 * number_of_colors)
        colors = []
        for i in range(0, number_of_colors):
            color = '#'
            for primary_color in (0, 1, 2):
                for primary_color_digit in (0, 1):
                    color += string[division_length * (i *\
                                                       6 + primary_color *\
                                                       2 + primary_color_digit)]
            colors.append(color)
        return(colors)
    else:
        raise(ValueError('The number of colors can not be more than ' +\
                        str(len(string) / 6)))


def _get_int_color(string, number_of_colors):
    if len(string) / 6 >= number_of_colors:
        division_length = len(string) / (6 * number_of_colors)
        colors = []
        for i in range(0, number_of_colors):
            color = [0,0,0]
            for primary_color in (0, 1, 2):
                for primary_color_digit in (0, 1):
                    color[primary_color] += int(string[division_length *\
                                                (i * 6 +\
                                                primary_color * 2 +\
                                                primary_color_digit)],16) *\
                                            primary_color_digit * 16
            colors.append(color)
        return(colors)
    else:
        raise(ValueError('The number of colors can not be more than ' +\
                        str(len(string) / 6)))