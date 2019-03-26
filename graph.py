import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import webcolors
from skimage import io
from os import walk

class HueValuePlot():

    def __init__(self):
        pass

    def create_dict_of_color_list(self, l):
        color_dict = {}
        for each in l:
            area, (r, g, b) = each
            color_dict[area] = (r, g, b)
        return color_dict

    def get_hue_value_from_list(self, color_list, rgb_dict):
        list_of_hue = []
        list_of_value = []
        list_of_rgb = []
        for each in color_list:
            area, (h, s, v) = each
            list_of_hue.append(h)
            list_of_value.append(v)
            list_of_rgb.append(rgb_dict[area])
        return list_of_hue, list_of_value, list_of_rgb

    def get_hex_from_rgb(self, triplet):
        return webcolors.rgb_to_hex(triplet)

    def plot_hue_and_value(self, list_of_hue, list_of_value, list_of_rgb, filename):
        f, (axarr1, axarr2) = plt.subplots(1, 2, figsize=(16, 9))
        # fig = plt.figure()
        # axarr2 = fig.add_subplot(2, 1, 0)
        # axarr1 = fig.add_subplot(2, 2, 0)


        for i,val in enumerate(list_of_hue):
            hex_color = self.get_hex_from_rgb(list_of_rgb[i])
            axarr2.scatter(list_of_hue[i], list_of_value[i], c=hex_color, s=80)
            axarr2.grid(color='#AFEEEE', linestyle='--', linewidth=0.5, )
        # plt.grid(color='#AFEEEE', linestyle='--', linewidth=0.5)
        # plt.xlabel('HUE')
        # plt.ylabel('VALUE / Lightness')
        # plt.ylim(0, 255)
        # plt.subplot(10)
        # plt.set_size_inches(8, 6)

        img = io.imread('images/'+filename)
        axarr1.axis('off')
        axarr1.imshow(img)

        plt.savefig('Output/'+filename, orientation='landscape', dpi=100)


if __name__ == '__main__':
    hueValuePlot = HueValuePlot()

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
        img = Image.open('images/'+filename).convert('RGB')
        c_rgb = img.getcolors()
        c_rgb = hueValuePlot.create_dict_of_color_list(c_rgb)
        img = img.convert('HSV')
        c = img.getcolors()
        list_of_hue, list_of_value, list_of_rgb = hueValuePlot.get_hue_value_from_list(c, c_rgb)
        # print(list_of_hue, list_of_value, list_of_rgb)
        hueValuePlot.plot_hue_and_value(list_of_hue, list_of_value, list_of_rgb, filename)
