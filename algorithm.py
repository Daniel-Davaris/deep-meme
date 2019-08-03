import keras
import sklearn
import cv2
from scraper import load_data
"""
in ->
[
    (score: INT(1-10), url)
]
"""


# TODO: Resize imagesd with cv2.resize()


model = keras.models.Sequential([
    # Conv block 1
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)), # retrofitted for demo (inputsize)
    keras.layers.Conv2D(32, (3, 3), activation='relu'),
    keras.layers.MaxPool2D(3, 3),

    # Conv block 2
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPool2D(3, 3),

    # Conv block 2
    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.MaxPool2D(3, 3),

    # Dense layer
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax') # retrofitted for demo (classifications)
])

model.summary()

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

his_train = model.fit_generator(load_data(), epochs=5, shuffle=True)


# result = model.predict(image)