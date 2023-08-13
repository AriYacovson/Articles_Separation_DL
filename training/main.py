from training.pdf2img import *
from training.preprocessing import *


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
    directory_open_and_convert_pdf_to_png(pdfs_directory_path, poppler_path, first_pages_path, other_pages_path)
    # writing the path of the directory that contains the separated pngs
    labeled_path = 'labeled_data'
    # writing the height and width of the images
    image_height, image_width = 224, 224
    # calling the function that opens the pngs and labels them
    X, y = open_resize_and_label_png_directory(labeled_path, image_width, image_height)
    # # testing the function
    # print(X.shape)
    # print(y.shape)
    # img = Image.fromarray(X[0]*255)
    # img.show()


if __name__ == '__main__':
    main()
