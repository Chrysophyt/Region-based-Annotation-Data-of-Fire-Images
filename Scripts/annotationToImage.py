# This script use VGG Image Annotator Tools with *.csv export type
# You can find more about the tools here https://www.robots.ox.ac.uk/~vgg/software/via/
# Load our project file and export it to *.csv, or other such as COCO json format.

#Params
Y_LEN, X_LEN = (400,256)
FILENAME = 'Video01_GT_'
CSV_FILE = 'Video01_csv.csv' 

#Parse csv data
import csv

data = []
with open(CSV_FILE, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

data = data[1:] #Remove header

#Draw annotation
import numpy as np
import cv2 as cv
import json
from PIL import Image

#Iterate for each data row
i_frame = 0
i_row = 0
while i_row < len(data):
    img = np.zeros((Y_LEN, X_LEN))
    img_name = data[i_row][0]
    n_region = data[i_row][3]

    #if there is no fire in frame
    if(int(n_region)==0):
        i_row+=1
    else:
        for i in range(int(n_region)):
            coords_data = json.loads(data[i_row][5])
            coords = []
            for coords_x, coords_y in zip(coords_data['all_points_x'], coords_data['all_points_y']):
                coords.append([coords_x, coords_y])
            cv.fillPoly(img, pts = np.int32([coords]), color =(255))
            i_row+=1

    i_frame+=1
    im = Image.fromarray(img).convert('RGB')
    im.save(FILENAME+str(i_frame).zfill(3)+'.jpg')