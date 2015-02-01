#!/usr/bin/env python

#
#	05-04-2014	by Taras Kuzyo
#
#

from __future__ import division
import hashlib
import argparse
import sys


try:
	import matplotlib.pyplot as pl 
	matplotlib_available = True
except ImportError:
	matplotlib_available = False

	try:
		from PIL import Image, ImageDraw, ImageOps
	except ImportError:	
		print('{0} needs either matplotlib or PIL module.'.format(sys.argv[0]))
		sys.exit(1)



def parse_args():
	'''
	parse_args() -> argparse

	Parses the standard args and 
	returns a configuration object.
	'''

	parser = argparse.ArgumentParser()

	parser.add_argument("string", help="A string to generate identicon.")

	return parser.parse_args()


def replicate(string, size):
	'''
	replicate(str, int) -> int

	Returns a string copied n times 
	needed for matrix generarion.
	'''
	n = 1 + size*size//len(string)

	return n*string


def generate_md5(string):
	'''
	generate_md5(str) -> str

	Returns MD5 sum of a string
	'''
	m = hashlib.md5()
	m.update(string.strip().lower())

	return m.hexdigest()


def get_hex_color(hexstring):
	'''
	get_hex_color(str) -> str
		
	Returns first six characters of MD5 sum as a color.
	'''
	return hexstring[0:6]


def hex_to_rgb(hex_value):
	'''
	hex_to_rgb(str) -> list

	Returns a RGB color value converted from hex string
	(in 0.0..1.0 range)
	'''
	return [ int(hex_value[i:i+2], 16) for i in range(0, len(hex_value), 2) ]


def make_matrix(hex_code, size, face='left'):
	'''
	make_matrix(str, int, str) -> list of lists

	Returns size x size square matrix generated from 
	hex code.
	'''

	color_offset = 6			# first 6 bytes for color
	data = [ [ hex_code[size*i + j + color_offset] for j in range(size) ] for i in range(size) ]

	if face   == 'left': 		# right half is the same as left
		for i in range(size):
			for j in range(size//2):
				data[i][-j-1] = data[i][j]

	elif face == 'right':		# left half is the same as right
		for i in range(size):
			for j in range(size//2):
				data[i][j] = data[i][-j-1]

	elif face == 'none':		# no symmetry -- leave as it is
		pass
	else:
		print("Unrecognized option '{" + leading + "}' ('right', 'left' or 'none' is expected) setting to 'none'.")

	return data


def pixel_map(matrix):
	'''
	pixel_map(list of lists) -> list of lists

	Returns a matrix with 0 or 1 depending of its hex value
	'''
	size = len(matrix)
	return [ [int(matrix[i][j], 16) % 2 for j in range(size)] for i in range(size) ]


def fill_ratio(matrix):
	'''
	fill_ratio(list of lists) -> float

	Returns a ratio of colored pixels to the total.
	'''
	size = len(matrix)
	return sum(matrix[i][j] for j in range(size) for i in range(size))/size**2


def create_image(filename, pixel_map, fg, bg = [255, 255, 255], transparent=False):
	'''
	create_image(str, list of lists, list, list, bool) -> NoneType

	Creates image with PIL module
	'''
	sc = 50
	size = len(pixel_map)
	image_size = sc*size

	fg_rgba = (fg[0], fg[1], fg[2], 255)						# non-transparent foreground
	bg_rgba = (bg[0], bg[1], bg[2], 255*int(not transparent))	# 0 for transparent = True, 1 for transparent = False

	im = Image.new('RGBA', (image_size, image_size), bg_rgba)
	draw = ImageDraw.Draw(im)

	[ draw.rectangle((i*sc, j*sc, (i+1)*sc, (j+1)*sc), fill=fg_rgba) 
		for i in range(size) for j in range(size) if pixel_map[i][j] ]

	im_with_border = ImageOps.expand(im, border=sc, fill=bg_rgba)
	im_with_border.rotate(90).save(filename)


def make_image(filename, pixel_map, fg, bg = [255, 255, 255], transparent=False):
	'''
	make_image(str, list of lists, list, list, bool) -> NoneType

	interpolations = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 
					'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 
					'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

	Creates image with matplotlib.pyplot.imshow 
	for given pixel matrix and fg and bg colors
	Saves an image with given filename
	'''
	
	# non-transparent foreground
	fg_rgba = (fg[0]/255, fg[1]/255, fg[2]/255, 1.0)
	# 0 for transparent = True, 1 for transparent = False						
	bg_rgba = (bg[0]/255, bg[1]/255, bg[2]/255, 1.0*int(not transparent))	

	size = len(pixel_map)
	image = [  [ fg_rgba if pixel_map[i][j] else bg_rgba for j in range(size) ] for i in range(size)  ]

	pl.axis('off')						#	disable axis
	pl.xticks(())						#	remove right margin
	pl.yticks(())						#	remove left margin

	interpolation = 'nearest'
	pl.imshow(image, interpolation=interpolation, origin='lower')
	pl.savefig(filename, bbox_inches='tight', transparent=transparent, pad_inches=0.5)


def generate_identicon(string, size, filename, bg=[255, 255, 255], face='left', transparent=True):
	'''
	generate_identicon(str, int, str, list, srt, bool) -> NoneType

	Generates corresplonding identicon for given string and size.
	Saves identicon as image.
	'''
	hex_string = replicate(string, size)

	hex_color = get_hex_color(string)
	rgb_color = hex_to_rgb(hex_color)
	
	matrix = make_matrix(hex_string, size, face)
	pixel = pixel_map(matrix)

	if matplotlib_available:
		make_image(filename, pixel, rgb_color, bg, transparent)
	else:
		create_image(filename, pixel, rgb_color, bg, transparent)


def main():
	'''
	main() -> NoneType

	Takes a string and generates an identicon for it.
	'''
	args = parse_args()

	string = args.string
	size = 7
	filename = string + '.png'

	generate_identicon(string, size, filename, face='left', transparent=True)


if __name__ == '__main__':
	main()


