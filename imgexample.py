## Little script that loads an image and that plays around with it

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

## JPEG image is loaded into a 3 dimensional numpy array
## There a triplet representing the level of Red, Green, Blue on a scale from 0 to 256 for each pixel of the image
image = mpimg.imread("examples/nuche.jpg")
## On our example the size of the array is 656 (height) x 534 (width) x 3 (RGB)
## If we want to access the green level on pixel 500, 200 (indexing starts at 0) we do it as follows:
image[500, 200, 1]

## This call returns the RGB triplet

image[500, 200, ]

## This returns the blue levels for the whole picture:
image[:, :, 2]

## This function creates a new window and prints the image on it:
def printimage(image):
    plt.imshow(image)
    plt.show()

## Close the window to carry on
printimage(image)

def only_one_color(image, color_index):
    buff = np.zeros(shape = image.shape, dtype = image.dtype)
    buff[:, :, color_index] = image[:, :, color_index]
    printimage(buff)
    return buff

## Only green
green_image = only_one_color(image, 1)

## Each color is the average of the three
def black_and_white(image):
    ## Need to convert to avoid overflow
    buff = image.astype(np.int32)
    # Averaging the three colors
    aver = (buff[:, :, 0] + buff[:, :, 1] + buff[:, :, 2]) / 3
    buff[:, :, 0] = aver
    buff[:, :, 1] = aver
    buff[:, :, 2] = aver
    buff = buff.astype(image.dtype)
    printimage(buff)
    return buff

## Print image in black and white
bw_image = black_and_white(image)

## switches the levels around. Default is Blue(2) -> Red(0), Red(0) -> Green(1), Green(1) -> Blue(2)
def change_colours_around(image, index_1 = 2, index_2 = 0, index_3 = 1):
    buff = image.copy()
    buff[:, :, 0] = image[:, :, index_1]
    buff[:, :, 1] = image[:, :, index_2]
    buff[:, :, 2] = image[:, :, index_3]
    printimage(buff)
    return(buff)

changed_image = change_colours_around(image)

# Image changed with another rule
changed_image2 = change_colours_around(image, index_1 = 0, index_2 = 2, index_3 = 1)

## Let the fun begin!!! :)

