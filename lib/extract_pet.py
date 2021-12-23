import os, sys
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path

files = sorted(os.listdir("./out/screenshots/"))

idx = 0
for file in files:

    ICON_WIDTH = 120
    ICON_HEIGHT = 120
    ICON_MARGIN_BOTTOM = 10
    ICON_SPACING = 17
    PAGE_LEFT_PADDIG = 14
    COL = 5
    ROW = 5

    filepath = "./out/screenshots/" + file

    img = cv.imread(filepath)
    (imgW, imgH) = img.shape[::2]

    blur = cv.bilateralFilter(img,9,75,75)
    imgray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(imgray,100,255, cv.THRESH_BINARY_INV)[1]
    contours, _ = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    largestSize = 0
    coord = (0,0)

    for c in contours:
        rect = cv.boundingRect(c)
        if cv.contourArea(c) > 10000: continue
        x,y,w,h = rect
        size = w * h
        if size > largestSize and size > 5000 and size < 15000:
            largestSize = w * h
            coord = (x,y)

    (x,y) = coord
    firstX = PAGE_LEFT_PADDIG
    firstY = y % (ICON_HEIGHT + ICON_MARGIN_BOTTOM + ICON_SPACING)

    if (ICON_HEIGHT + ICON_SPACING) * ROW + firstY > imgH:
        ROW = ROW - 1

    for i in range(COL):
        for j in range(ROW):
            x1 = firstX + (i * ICON_WIDTH) + i * ICON_SPACING
            y1 = firstY + (j * (ICON_HEIGHT + ICON_MARGIN_BOTTOM)) + j * ICON_SPACING
            x2 = x1 + ICON_WIDTH
            y2 = y1 + ICON_HEIGHT
            crop_img = img[y1:y2, x1:x2]
            cv.imwrite('./out/cropped/' + str(idx) + '.jpg', crop_img)
            idx += 1