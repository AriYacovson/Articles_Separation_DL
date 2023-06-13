import tensorflow as tf
import numpy as np
from preprocessing import *

# Load the saved model
model = tf.keras.models.load_model('third_model.h5')

# Load the data
X, y = open_resize_and_label_png_directory('labeled_data', 224, 224)
y = np.where(y == 'first_pages', 1, 0)

# Get the model predictions
y_pred = model.predict(X)
print(y_pred)

# Get the predicted classes
y_pred_classes = (y_pred > 0.5).astype("int32")

# Get the true classes
y_true_classes = y

# Get the mistakes
mistakes = np.where(y_pred_classes != y)[0]

# Get the mistakes images
mistakes_images = X[mistakes]

print(mistakes_images.shape)
# Get the mistakes labels
mistakes_labels = y[mistakes]

# Get the mistakes predictions
mistakes_predictions = y_pred[mistakes]

# saving the mistakes images and labels
# for i in range(len(mistakes)):
#     img = Image.fromarray(mistakes_images[i] * 255)
#     img.save('mistakes_images/' + str(i) + 'labeled as' + 'mistakes_labels' + '.png')


# def finding_and_saving_model_mistakes(model, X_test, y_test, mistakes_directory_path):
#     """
#     finds the mistakes of the model and saves them in a directory
#     :param model:
#     :param X_test:
#     :param y_test:
#     :return:
#     """
#
#     # Load the saved model
#     model = tf.keras.models.load_model('path_to_saved_model')
#
#     # Get the model predictions
#     predictions = model.predict(X_test)
#
#     # Get the predicted classes
#     predicted_classes = np.argmax(predictions, axis=1)
#
#     # Get the true classes
#     true_classes = np.argmax(y_test, axis=1)
#
