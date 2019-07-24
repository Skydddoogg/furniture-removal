import numpy as np
import pandas as pd
import cv2
from PIL import Image
import os
from skimage import morphology
from skimage import io

from config import img_name, considered_obj

img_path = os.path.join('ADE20K_2016_07_26', 'images', 'training', 'b', 'bedroom', img_name + '.jpg')
original_img = Image.open(img_path)
original_img = np.array(original_img)

segment_class = np.load('loaded_segmentation/oi.npy')
segment_class_name = pd.read_csv('loaded_segmentation/objects.csv')

segmented_imgs = list()

for i in np.unique(segment_class):
    if (segment_class_name['class'].iloc[int(i) - 1] in considered_obj) and (int(i) != 0):
        prediction_mask = (segment_class == i)
        prediction_box = (segment_class == i)
        prediction_box = prediction_box.astype(np.uint8)
        prediction_box = prediction_box*255

        cropped_object = original_img * np.dstack((prediction_mask,) * 3)
        square = morphology.square(5)
        temp = morphology.binary_erosion(prediction_mask, square)
        negative_mask = (temp != True)
        eroding_countour = negative_mask * prediction_mask
        eroding_countour_img = np.dstack((eroding_countour, ) * 3)
        cropped_object[eroding_countour_img] = 248
        png_transparancy_mask = np.uint8(prediction_mask * 255)
        image_shape = cropped_object.shape
        png_array = np.zeros(shape=[image_shape[0], image_shape[1], 4], dtype=np.uint8)
        png_array[:, :, :3] = cropped_object
        png_array[:, :, 3] = png_transparancy_mask

        path_to_save = os.path.join('extracted_segments', img_name + str(i) + '.png')
        segmented_imgs.append(path_to_save)
        io.imsave(path_to_save, png_array)

network_input = Image.open(img_path)
network_input = network_input.convert('RGBA')

network_input_data = network_input.load()

for segmented_img in segmented_imgs:
    segmented = Image.open(segmented_img)
    segmented = segmented.convert('RGB')
    segmented_data = segmented.load()

    for y in range(segmented.size[1]):
        for x in range(segmented.size[0]):
            if segmented_data[x, y] != (0, 0, 0):
                network_input_data[x, y] = (255, 255, 255, 255)
                segmented_data[x, y] = (0, 0, 0)
            else:
                segmented_data[x, y] = (255, 255, 255)
    segmented.save('masks/' + segmented_img.split('/')[1].split('.png')[0] + '.jpg')

network_input.save('network_input/' + img_name + '.png')