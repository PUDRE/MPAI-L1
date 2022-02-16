import argparse
from matplotlib import pyplot as plt
from skimage.io import imshow, show, imread, imsave
from skimage import data, segmentation
from skimage.exposure import histogram

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str)
parser.add_argument('-s', '--spath', type=str)
parser.add_argument('-x', '--xpixel', type=int)
parser.add_argument('-y', '--ypixel', type=int)
parser.add_argument('-c', '--color', type=int)

args = parser.parse_args()
img = imread(args.path)

imshow(img)

show()
