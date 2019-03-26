import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import webcolors
from sklearn.cluster import MiniBatchKMeans

from skimage import io
from os import walk
from mpl_toolkits.mplot3d import axes3d

color_dict = { '0' : 'red',
               '1' : 'blue',
               '2' : 'green',
               '3' : 'black',
               '4' : 'cyan',
               '5' : 'grey'}

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
        list_of_saturation = []
        list_of_rgb = []
        for each in color_list:
            area, (h, s, v) = each
            list_of_hue.append(h)
            list_of_value.append(v)
            list_of_saturation.append(s)
            list_of_rgb.append(rgb_dict[area])
        return list_of_hue, list_of_value, list_of_rgb, list_of_saturation

    def get_hex_from_rgb(self, triplet):
        return webcolors.rgb_to_hex(triplet)

    def plot_hue_and_value(self, list_of_hue, list_of_value, list_of_rgb, list_of_saturation, filename, labels):
        # f, (axarr1, axarr2) = plt.subplots(1, 2, figsize=(16, 9))
        fig = plt.figure()
        # ax1, ax2 = fig.add_subplot(1, 2, figsize=(16, 9))
        # ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
        ax = fig.gca(projection='3d')

        for i, val in enumerate(list_of_hue):
            hex_color = self.get_hex_from_rgb(list_of_rgb[i])
            ax.scatter(list_of_hue[i], list_of_value[i], list_of_saturation[i], c=hex_color, edgecolor=color_dict[str(labels[i])] , linewidths= 2, s=80, label=labels[i])
            ax.grid(color='#AFEEEE', linestyle='--', linewidth=0.5, )
        # plt.grid(color='#AFEEEE', linestyle='--', linewidth=0.5)
        plt.xlabel('HUE')
        plt.ylabel('VALUE / Lightness')
        # plt.zlabel('')
        # plt.show()
        # plt.ylim(0, 255)
        # plt.subplot(10)
        # plt.set_size_inches(8, 6)

        # img = io.imread(filename)
        # axarr1.axis('off')
        # axarr1.imshow(img)
        # plt.show()

        plt.savefig('Output/'+filename, orientation='landscape', dpi=200)


if __name__ == '__main__':
    hueValuePlot = HueValuePlot()
    # filename = 's250-2False5c4Miami-Heat.processed.png'
    # img = Image.open(filename).convert('RGB')
    # c_rgb = img.getcolors()
    # c_rgb = hueValuePlot.create_dict_of_color_list(c_rgb)
    # img = img.convert('HSV')
    # c = img.getcolors()
    # print(c)
    # list_of_hue, list_of_value, list_of_rgb, list_of_saturation = hueValuePlot.get_hue_value_from_list(c, c_rgb)
    # h_list = np.array(list_of_hue)
    # s_list = np.array(list_of_saturation)
    # v_list = np.array(list_of_value)
    # training_array = np.dstack((h_list, s_list, v_list))
    # training_array = training_array.reshape(-1, 3)
    # print(training_array.shape, training_array)
    # clt = MiniBatchKMeans(n_clusters=5)
    # labels = clt.fit_predict(training_array)
    # print(labels)
    # hueValuePlot.plot_hue_and_value(list_of_hue, list_of_value, list_of_rgb, list_of_saturation, filename, labels)
    #
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
        list_of_hue, list_of_value, list_of_rgb, list_of_saturation = hueValuePlot.get_hue_value_from_list(c, c_rgb)
        h_list = np.array(list_of_hue)
        s_list = np.array(list_of_saturation)
        v_list = np.array(list_of_value)
        training_array = np.dstack((h_list, s_list, v_list))
        training_array = training_array.reshape(-1, 3)
        # print(training_array.shape, training_array)
        clt = MiniBatchKMeans(n_clusters=5)
        labels = clt.fit_predict(training_array)
        # print(labels)
        hueValuePlot.plot_hue_and_value(list_of_hue, list_of_value, list_of_rgb, list_of_saturation, filename, labels)