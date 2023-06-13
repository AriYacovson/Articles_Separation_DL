import PIL.ImageShow
import time
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

from pdf2img import *
from preprocessing import *




def main():
    # writing the path of the directory that contains the pdfs
    pdfs_directory_path = 'Articles_Examples'
    # writing the path of the poppler
    poppler_path = r"C:\Users\ariya\Downloads\Release-23.05.0-0\poppler-23.05.0\Library\bin"
    # writing the path of the directory that contains the first pages of the pdfs
    first_pages_path = r'labeled_data\first_pages'
    # writing the path of the directory that contains the other pages of the pdfs
    other_pages_path = r'labeled_data\other_pages'

    # calling the function that converts the pdfs to pngs and saves them in the directories
    # directory_open_and_convert_pdf_to_png(pdfs_directory_path, poppler_path, first_pages_path, other_pages_path)

    # writing the path of the directory that contains the separated pngs
    labeled_path = 'labeled_data'
    # writing the height and width of the images
    image_height, image_width = 224, 224

    # timing how long it takes to open, resize and label the pngs
    start_time = time.time()
    # it could take about 2 - 3 minutes
    X, y = open_resize_and_label_png_directory(labeled_path, image_height, image_width)
    y = np.where(y == 'first_pages', 1, 0)
    # printing the time it took to open, resize and label the pngs
    print("--- %s seconds --- till open and preprocessed" % (time.time() - start_time))

    # # testing the function
    # print(X.shape)
    # print(y.shape)
    # img = Image.fromarray(X[0]*255)
    # img.show()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Print the shape of the training data
    print('X_train shape:', X_train.shape, 'y_train shape:', y_train.shape)
    # Print the shape of the testing data
    print('X_test shape:', X_test.shape, 'y_test shape:', y_test.shape)

    # timing how long it take to define the model
    start_time = time.time()

    # Define the model
    model = tf.keras.Sequential()

    # Add a convolutional layer with 32 filters, a 3x3 kernel, and 'relu' activation
    model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(image_height, image_width, 1)))

    # Add a max pooling layer with 2x2 pool size
    model.add(layers.MaxPooling2D((2, 2)))

    # Add another convolutional layer with 64 filters and 'relu' activation
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    # Flatten the output from the previous layer
    model.add(layers.Flatten())

    # Add a dense (fully connected) layer with 64 units and 'relu' activation
    model.add(layers.Dense(32, activation='relu'))

    # Add an output layer with 1 unit and 'sigmoid' activation for binary classification
    model.add(layers.Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # printing the time it took to define the model
    print("--- %s seconds --- till defining the model" % (time.time() - start_time))

    # Define the number of epochs and batch size
    epochs = 10
    batch_size = 16
    # timing how long it takes to train the model
    start_time = time.time()

    # Train the model
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=batch_size)

    # Evaluate the model on the test data
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    # Print out the model's accuracy
    print('\nTest loss:', test_loss)
    print('Test accuracy:', test_accuracy)

    # printing the time it took to train the model
    print("--- %s seconds --- till training the model" % (time.time() - start_time))

    # Print the model summary
    print(model.summary())

    # Save the model to h5 file
    model.save('third_model.h5')


if __name__ == '__main__':
    main()
