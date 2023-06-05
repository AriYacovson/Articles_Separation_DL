import os
from PIL import Image
import numpy as np

# Set the path to your dataset directory
dataset_dir = 'labeled_data'

# Set the desired image dimensions
image_width, image_height = 224, 224

# Initialize lists to store images and labels
images = []
labels = []

# Loop through the dataset directory
for root, dirs, files in os.walk(dataset_dir):
    for file in files:
        # Load the image using PIL
        image_path = os.path.join(root, file)
        image = Image.open(image_path)

        # Resize the image
        image = image.resize((image_width, image_height))

        # Normalize the pixel values to [0, 1]
        image = np.array(image) / 255.0

        # Append the image and label to the respective lists
        images.append(image)

        # Extract the label from the directory name
        label = os.path.basename(root)
        labels.append(label)

# Convert the lists to NumPy arrays
images = np.array(images)
labels = np.array(labels)

# Print the shapes of the images and labels arrays
print('Images shape:', images.shape)
print('Labels shape:', labels.shape)
