# -*- coding: utf-8 -*-
"""VGG16

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QsQN2OID5B1TC-qXPXVcQd8maFOMctFD
"""

import zipfile

zip_path = '/content/archive (1).zip'

# Extract the dataset
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('catdog_dataset')

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import VGG19
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Training and Validation Data Generators
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)  # 20% for validation

# Load Training Data (80% of train folder)
train_generator = train_datagen.flow_from_directory(
    '/content/catdog_dataset/training_set',    # Path to training data
    target_size=(224, 224), # Resize images
    batch_size=32,          # Batch size
    class_mode='binary',    # Binary classification (Cats vs. Dogs)
    subset='training'       # Use only training subset
)

# Load Validation Data (20% of train folder)
val_generator = train_datagen.flow_from_directory(
    '/content/catdog_dataset/training_set',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'      # Use only validation subset
)

# Testing Data Generator (Without Validation Split)
test_datagen = ImageDataGenerator(rescale=1./255)  # Only rescale, no split

test_generator = test_datagen.flow_from_directory(
    '/content/catdog_dataset/test_set',       # Path to test data
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',   # Or 'None' if test labels are unavailable
    shuffle=False          # Don't shuffle test data (important for predictions)
)

base_model = VGG19(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model
base_model.trainable = False

# Create the model
model = models.Sequential([
    base_model,
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),  # Dropout for regularization
    layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the Model
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=2  # You can increase the number of epochs for better performance
)

# Plot Training & Validation Accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Train Accuracy', marker='o')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy', marker='s')

plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training vs. Validation Accuracy (VGG19)')
plt.legend()
plt.grid(True)
plt.show()

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_generator)
print(f"Test accuracy: {test_acc:.4f}")

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Training and Validation Data Generators
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)  # 20% for validation

# Load Training Data (80% of train folder)
train_generator = train_datagen.flow_from_directory(
    '/content/catdog_dataset/training_set',    # Path to training data
    target_size=(224, 224), # Resize images
    batch_size=32,          # Batch size
    class_mode='binary',    # Binary classification (Cats vs. Dogs)
    subset='training'       # Use only training subset
)

# Load Validation Data (20% of train folder)
val_generator = train_datagen.flow_from_directory(
    '/content/catdog_dataset/training_set',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'      # Use only validation subset
)

# Testing Data Generator (Without Validation Split)
test_datagen = ImageDataGenerator(rescale=1./255)  # Only rescale, no split

test_generator = test_datagen.flow_from_directory(
    '/content/catdog_dataset/test_set',       # Path to test data
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',   # Or 'None' if test labels are unavailable
    shuffle=False          # Don't shuffle test data (important for predictions)
)

model = models.Sequential([
    # Layer 1: Convolutional Layer with 96 filters, kernel size 11x11, stride 4
    layers.Conv2D(96, (11, 11), strides=(4, 4), activation='relu', input_shape=(224, 224, 3)),
    # Layer 2: Max Pooling Layer with pool size 3x3 and stride 2
    layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2)),
    # Layer 3: Convolutional Layer with 256 filters, kernel size 5x5, padding 'same'
    layers.Conv2D(256, (5, 5), padding='same', activation='relu'),
    # Layer 4: Max Pooling Layer with pool size 3x3 and stride 2
    layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2)),
    # Layer 5: Convolutional Layer with 384 filters, kernel size 3x3, padding 'same'
    layers.Conv2D(384, (3, 3), padding='same', activation='relu'),
    # Layer 6: Convolutional Layer with 384 filters, kernel size 3x3, padding 'same'
    layers.Conv2D(384, (3, 3), padding='same', activation='relu'),
    # Layer 7: Convolutional Layer with 256 filters, kernel size 3x3, padding 'same'
    layers.Conv2D(256, (3, 3), padding='same', activation='relu'),
    # Layer 8: Max Pooling Layer with pool size 3x3 and stride 2
    layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2)),
    # Layer 9: Flatten the output for fully connected layers
    layers.Flatten(),
    # Layer 10: Fully Connected Layer with 4096 units
    layers.Dense(4096, activation='relu'),
    # Layer 11: Dropout Layer with 50% dropout rate
    layers.Dropout(0.5),
    # Layer 12: Fully Connected Layer with 4096 units
    layers.Dense(4096, activation='relu'),
    # Layer 13: Dropout Layer with 50% dropout rate
    layers.Dropout(0.5),
    # Layer 14: Output Layer with 1 unit and sigmoid activation for binary classification
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Print the model summary
model.summary()

# Train the Model
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=2  # You can increase the number of epochs for better performance
)

# Plot Training & Validation Accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Train Accuracy', marker='o')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy', marker='s')

plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training vs. Validation Accuracy (AlexNet)')
plt.legend()
plt.grid(True)
plt.show()

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_generator)
print(f"Test accuracy: {test_acc:.4f}")

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Training and Validation Data Generators
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)  # 20% for validation

# Load Training Data (80% of train folder)
train_generator = train_datagen.flow_from_directory(
    '/content/catdog_dataset/training_set',    # Path to training data
    target_size=(224, 224), # Resize images
    batch_size=32,          # Batch size
    class_mode='binary',    # Binary classification (Cats vs. Dogs)
    subset='training'       # Use only training subset
)

# Load Validation Data (20% of train folder)
val_generator = train_datagen.flow_from_directory(
    '/content/catdog_dataset/training_set',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'      # Use only validation subset
)

# Testing Data Generator (Without Validation Split)
test_datagen = ImageDataGenerator(rescale=1./255)  # Only rescale, no split

test_generator = test_datagen.flow_from_directory(
    '/content/catdog_dataset/test_set',       # Path to test data
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',   # Or 'None' if test labels are unavailable
    shuffle=False          # Don't shuffle test data (important for predictions)
)
def inception_module(x, filters):
    # 1x1 Convolution
    conv1x1 = layers.Conv2D(filters, (1, 1), padding='same', activation='relu')(x)

    # 3x3 Convolution
    conv3x3 = layers.Conv2D(filters, (3, 3), padding='same', activation='relu')(x)

    # 5x5 Convolution
    conv5x5 = layers.Conv2D(filters, (5, 5), padding='same', activation='relu')(x)

    # Max Pooling
    max_pool = layers.MaxPooling2D((3, 3), strides=(1, 1), padding='same')(x)
    max_pool = layers.Conv2D(filters, (1, 1), padding='same', activation='relu')(max_pool)

    # Concatenate all branches
    output = layers.concatenate([conv1x1, conv3x3, conv5x5, max_pool], axis=-1)
    return output

# Define the GoogleNet (InceptionV1) model
input_layer = layers.Input(shape=(224, 224, 3))

# Initial Convolution and Pooling
x = layers.Conv2D(64, (7, 7), strides=(2, 2), padding='same', activation='relu')(input_layer)
x = layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)
x = layers.Conv2D(192, (3, 3), padding='same', activation='relu')(x)
x = layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)

# Inception Modules
x = inception_module(x, filters=64)
x = inception_module(x, filters=128)
x = layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)
x = inception_module(x, filters=192)
x = inception_module(x, filters=256)
x = layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)

# Fully Connected Layers
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dense(1024, activation='relu')(x)
x = layers.Dropout(0.4)(x)
output_layer = layers.Dense(1, activation='sigmoid')(x)

# Create the model
model = models.Model(inputs=input_layer, outputs=output_layer)

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Print the model summary
model.summary()

# Train the Model
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=2  # You can increase the number of epochs for better performance
)

# Plot Training & Validation Accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Train Accuracy', marker='o')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy', marker='s')

plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training vs. Validation Accuracy (GoogleNet)')
plt.legend()
plt.grid(True)
plt.show()

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_generator)
print(f"Test accuracy: {test_acc:.4f}")

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50  # Import ResNet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)  # 20% for validation

# Load Training Data (80% of train folder)
train_generator = train_datagen.flow_from_directory(
    '/content/catdog_dataset/training_set',    # Path to training data
    target_size=(224, 224), # Resize images
    batch_size=32,          # Batch size
    class_mode='binary',    # Binary classification (Cats vs. Dogs)
    subset='training'       # Use only training subset
)

# Load Validation Data (20% of train folder)
val_generator = train_datagen.flow_from_directory(
    '/content/catdog_dataset/training_set',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'      # Use only validation subset
)

# Testing Data Generator (Without Validation Split)
test_datagen = ImageDataGenerator(rescale=1./255)  # Only rescale, no split

test_generator = test_datagen.flow_from_directory(
    '/content/catdog_dataset/test_set',       # Path to test data
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',   # Or 'None' if test labels are unavailable
    shuffle=False          # Don't shuffle test data (important for predictions)
)
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model
base_model.trainable = False

# Create the model
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),  # Global Average Pooling to reduce spatial dimensions
    layers.Dense(256, activation='relu'),  # Fully Connected Layer
    layers.Dropout(0.5),  # Dropout for regularization
    layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Print the model summary
model.summary()

# Train the Model
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=2  # You can increase the number of epochs for better performance
)

# Plot Training & Validation Accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label='Train Accuracy', marker='o')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy', marker='s')

plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training vs. Validation Accuracy (ResNet50)')
plt.legend()
plt.grid(True)
plt.show()

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_generator)
print(f"Test accuracy: {test_acc:.4f}")