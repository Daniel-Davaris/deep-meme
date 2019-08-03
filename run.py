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
print(image)
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

image = cv2.resize((100, 100))
pred = model.evaluate([image])[0]

plt.bar(np.arange(10), pred)

plt.show()
