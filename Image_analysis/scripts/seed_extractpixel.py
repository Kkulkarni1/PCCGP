# Author: Roshan Kulkarni
# Idea based of code from Adrian Rosebrock (Pyimagesearch) -- Deteriming object color
# Usage: python seed_extractpixel.py -i /path/Image.bmp -c Image-C.bmp -o1 Image-pixel.txt -o2 Image-mean_pixel.txt
# This script extracts pixel information in RGB from peanut seed images

# import the necessary packages
from __future__ import print_function
import imutils
import cv2
import argparse
import numpy as np
from PIL import Image

# Function that returns output image file with prefix file name
def name_img():
    img_input = Image.open(args["image"])
    return(img_input.filename)

# Constructing argument parser
ap = argparse.ArgumentParser()
# input image file
ap.add_argument("-i", "--image", required=True, help="path to input image")
# File with counts
ap.add_argument("-c", "--count_image", required=False)
# Extract individual pixels within each seed
ap.add_argument("-o1", "--out_file_1", required=True)
# Extract mean pixel vales for each seed
ap.add_argument("-o2", "--out_file_2", required=True)
args = vars(ap.parse_args())

# Reading input image
image = cv2.imread(args["image"])
# Converting image to gray scale
gray_init = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
graymask = cv2.inRange(gray_init, 187, 255)
grayres = cv2.bitwise_and(gray_init, gray_init, mask=graymask)
image3 = image
image3[graymask>173] = (0,0,0)
# Setting threshold (threshold value can change based on image)
gray = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 127, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Finding contours
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# Defining empty list
lst_intensities = []

# Looping through contours and drawing contours
for i in range(len(cnts)):
    # Create a mask image that contains the contour filled in
    if cv2.contourArea(cnts[i]) > 1000:
        #print(cv2.contourArea(cnts[i]))
        cimg = np.zeros_like(image)
        cv2.drawContours(cimg, cnts, i, color=255, thickness=-1)
        # Access the image pixels and create a 1D numpy array then add to list
        pts = np.where(cimg == 255)
        lst_intensities.append(image[pts[0], pts[1]])
# Writing output files
outfile_1 = open(args["out_file_1"], 'w')
outfile_2 = open(args["out_file_2"], 'w')
outfile_1.write("%s \t %s \t %s \t %s \t %s \n" % ("Seed_No", "Accession", "Blue_Pixel", "Green_pixel", "Red_pixel"))
outfile_2.write("%s \t %s \t %s \t %s \t %s \n" % ("Seed_No", "Accession", "Mean_Blue_Pixel", "Mean_Green_pixel", "Mean_Red_pixel"))

# Setting the counters
count_mean = 0
count = 1
red = 0
green = 0
blue = 0
# Looping through the list with pixel values to caluclate mean
for i in lst_intensities:
    total_red = 0
    total_green = 0
    total_blue = 0
    for j in range(len(i)):
        blue = i[j][0]
        green = i[j][1]
        red = i[j][2]
        total_blue += i[j][0]
        total_green += i[j][1]
        total_red += i[j][2]
        outfile_1.write("%i \t %s \t %f \t %f \t %f \n" % (count, name_img(), blue, green, red))
    count = count + 1
    mean_blue = total_blue / len(i)
    mean_green = total_green / len(i)
    mean_red = total_red/ len(i)
    count_mean = count_mean + 1
    outfile_2.write("%i \t %s \t %f \t %f \t %f \n" % (count_mean, name_img(), mean_blue, mean_green, mean_red))

#loop over the contours
for (i, c) in enumerate(cnts):
    if cv2.contourArea(cnts[i]) > 1000:
       #draw the contour
       ((x, y), _) = cv2.minEnclosingCircle(c)
       cv2.putText(image, "#{}".format(i + 1), (int(x) - 10, int(y)),
       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
       cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
cv2.imwrite(args["count_image"], image)




