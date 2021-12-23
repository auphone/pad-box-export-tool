import glob, os
import sys
import time
import json
import math
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(8)

srcDir = "./pets"
boxDir = "./out/cropped"
DEBUG = False

start_time = time.time()
srcImgs = sorted(os.listdir(srcDir))
boxImgs = sorted(os.listdir(boxDir))


# Initiate SIFT detector
sift = cv.SIFT_create()
matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)

# prepare src images
def genSrc(filename):
    srcImg = srcDir + "/" + filename
    img = cv.imread(srcImg,cv.IMREAD_GRAYSCALE)
    kp, des = sift.detectAndCompute(img,None)
    h, w = img.shape
    cols = math.ceil(w / 98)
    rows = math.ceil(h / 98)
    id = int(filename.split(".")[0])
    return (img, kp, des, id)

srcs = pool.map(genSrc, srcImgs)
print("--- Before match: %s seconds ---" % (time.time() - start_time))

# Results
def run(videoImg):

    # Prepare video image
    print(boxDir + "/" + videoImg)

    img2 = cv.imread(boxDir + "/" + videoImg,cv.IMREAD_GRAYSCALE) # trainImage
    kp2, des2 = sift.detectAndCompute(img2,None)

    # Start comparing
    maxscore = 0
    maxid = 0
    cachesrc = None
    for srcIdx, src in enumerate(srcs):

        img1, kp1, des1, id = src
        matches = matcher.knnMatch(des1,des2,k=2)

        score = 0
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                score += 1

        if score > 15 and score > maxscore:
            maxscore = score
            maxid = id

            if DEBUG:
                cachesrc = src

    if DEBUG and cachesrc:
        img1, kp1, des1, id = cachesrc
        fig = plt.figure()
        fig.add_subplot(1, 2, 1)
        plt.imshow(img1)
        fig.add_subplot(1, 2, 2)
        plt.imshow(img2)
        plt.savefig('./out/match_results/' + videoImg)
        return id
    else:
        return maxid

results = pool.map(run, boxImgs)

print("--- After loop %s seconds ---" % (time.time() - start_time))


# Result
idStr = ""
for res in np.unique(list(filter(None, results))):
    idStr += (str(res) + ",")

idStr = idStr[:-1]
f = open("./out/ids.txt", "w")
f.write(idStr)
f.close()