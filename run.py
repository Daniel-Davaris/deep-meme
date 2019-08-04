import argparse
import keras
from data_prep import pull_img_web
import matplotlib.pyplot as plt
import requests
import numpy as np
import cv2

model = keras.models.load_model("model.h5")

parser = argparse.ArgumentParser()
parser.add_argument("url")
url = parser.parse_args().url

# pull image
resp = requests.get(url)
image = np.asarray(bytearray(resp.content), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
print(image.shape)
plt.subplot(1, 2, 1)
plt.imshow(image)

image = cv2.resize(image, (100, 100))

pred = model.predict(np.array([image]).reshape(1, 100, 100, 3))[0]
plt.subplot(1, 2, 2)
plt.bar(np.arange(10), pred)
plt.show()

## SAMPLE COMMAND:
## python run.py https://i.redd.it/odqm10rab9a31.jpg
