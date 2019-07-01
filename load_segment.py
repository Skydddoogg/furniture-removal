import scipy.io
import cv2
import matlab.engine
import numpy as np
import os
import pandas as pd

from config import img_name

eng = matlab.engine.start_matlab()

img_path = os.path.join('ADE20K_2016_07_26', 'images', 'training', 'b', 'bedroom', img_name + '.jpg')

img = cv2.imread(img_path)

Om, Oi, Pm, Pi, objects, parts = eng.loadAde20K(img_path, nargout=6)

np.save('loaded_segmentation/om.npy', np.array(Om))
np.save('loaded_segmentation/oi.npy', np.array(Oi))
np.save('loaded_segmentation/pm.npy', np.array(Pm))
np.save('loaded_segmentation/pi.npy', np.array(Pi))

df_objects = pd.DataFrame.from_dict(objects)
df_parts = pd.DataFrame.from_dict(parts)

df_objects.to_csv('loaded_segmentation/objects.csv')
df_parts.to_csv('loaded_segmentation/parts.csv')