from os import walk
import cv2
import numpy as np


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

f = []
for (dirpath, dirnames, filenames) in walk('images'):
    f.extend(filenames)
    break

counter = 0
for each in f:
    # name = each
    print("processing image", counter)
    counter += 1
    filename = each
    img = cv2.imread('Output/'+filename)
    img = image_resize(img, height=1200)
    main_img = cv2.imread('images/'+filename)
    joined = np.hstack((main_img, img))
    cv2.imwrite('final/'+filename, joined)