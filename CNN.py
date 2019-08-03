import keras
from sklearn.model_selection import train_test_split
import cv2
# from scraper import load_data
import matplotlib.pyplot as plt
import h5py
import numpy as np

"""
in ->
[
    (score: INT(1-10), url)
]
"""

## Graphing


def plot_train(history):
    plt.subplot(1, 2, 1)
    plt.title("Loss")
    plt.plot(history.history['loss'], label="Training")
    plt.plot(history.history['val_loss'], label="Validation")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.title("Accuracy")
    plt.plot(history.history['acc'], label="Training")
    plt.plot(history.history['val_acc'], label="Validation")
    plt.legend()

    plt.show()


# TODO: Resize imagesd with cv2.resize()

model = keras.models.Sequential([
    # Conv block 1
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)), 
    keras.layers.Conv2D(32, (3, 3), activation='relu'),
    keras.layers.MaxPool2D(2, 2),

    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPool2D(2, 2),

    # Conv block 2
    keras.layers.Conv2D(96, (3, 3), activation='relu'),
    keras.layers.Conv2D(96, (3, 3), activation='relu'),
    keras.layers.MaxPool2D(4, 4),

    # Dense layer
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'),
    # keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax') 
])

model.summary()

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)
hf = h5py.File('data.h5', 'r')
y, t_y, x, t_x = train_test_split(np.array(hf.get('labels')), np.array(hf.get('imgs')), test_size=0.15)
print(y[1])

history = model.fit(x, y, epochs=150, shuffle=True, validation_data=(t_x, t_y), batch_size=20)

plot_train(history)

# result = model.predict(image)
