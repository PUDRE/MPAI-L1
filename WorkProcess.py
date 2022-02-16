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
flooded = segmentation.flood_fill(img, (args.xpixel, args.ypixel), args.color)
imsave(args.spath, flooded)

fig = plt.figure(figsize=(10, 5))

fig.add_subplot(2, 2, 1)
imshow(img)

fig.add_subplot(2, 2, 2)
imshow(flooded)

hist_red, bins_red = histogram(img[500:600, 300:400])
fig.add_subplot(2, 2, 3)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)

hist_red, bins_red = histogram(flooded[500:600, 300:400])
fig.add_subplot(2, 2, 4)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)

show()
