# image_parroter/thumbnailer/tasks.py

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.

import matplotlib.pyplot as plt
import seaborn as sns
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout , BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from keras.callbacks import ReduceLROnPlateau
import cv2
import os
import pickle

import os
from zipfile import ZipFile
from celery import shared_task
from PIL import Image
from django.conf import settings
from pathlib import Path

@shared_task
def make_thumbnails(file_path, thumbnails=[]):
    path, file = os.path.split(file_path)
    file_name, ext = os.path.splitext(file)
    zip_file = f"{file_name}.zip"
    results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
    try:
        zipper = ZipFile(path+'/'+zip_file, 'w')
        # labels = ['PNEUMONIA', 'NORMAL']
        img_size = 150

        x1 = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        x2 = cv2.resize(x1, (img_size, img_size))  # Reshaping images to preferred size
        x3 = np.array(x2) / 255
        x3 = x3.reshape(-1, img_size, img_size, 1)

        #history = pickle.load(open('trainHistoryDict', "rb"))
        ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).resolve().parents[1].__str__()
        model = keras.models.load_model(ROOT_DIR+'\image_pnev\model_01')
        model.load_weights(ROOT_DIR+'\image_pnev\model_weights_01')

        predictions = model.predict(x3)
        predictions = predictions.reshape(1, -1)[0]

        fig = plt.figure(figsize=(10, 10))
        plt.imshow(x1, cmap='gray')
        plt.title("Predicted Class {}".format(predictions[0])+'1 - normal, 0 - bad')

        fig.savefig(file_path)
        os.chdir(settings.IMAGES_DIR)
        zipper.write(file)
        os.remove(file_path)
        zipper.close()
    except IOError as e:
        print(e)
    return results