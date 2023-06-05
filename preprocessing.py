import os
from PIL import Image
import numpy as np


def open_resize_and_label_png_directory(input_directory_path, image_width, image_height):
    """
    gets a directory of png files, resizing them into the desired size
    :param input_directory_path:
    :param image_width:
    :param image_height:
    :type input_directory_path: string
    :type image_width: integer
    :type image_height: integer
    :return: images
    :return: labels
    :rtype images: list
    :rtype labels: list
    """

    # Initialize lists to store images and labels
    images = []
    labels = []

    # Loop through the dataset directory
    for root, dirs, files in os.walk(input_directory_path):
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

    # Return the images and labels
    return images, labels
