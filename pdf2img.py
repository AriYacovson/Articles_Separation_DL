import os
from pdf2image import convert_from_path


def directory_open_and_convert_pdf_to_png(input_directory_path, poppler_path,
                                          first_pages_directory_path, other_pages_directory_path):
    """
    gets a directory of pdf files, converting them into png
    and saving them to two classes - first_pages and other_pages
    :param input_directory_path:
    :param poppler_path:
    :param first_pages_directory_path:
    :param other_pages_directory_path:
    :type input_directory_path: string
    :type first_pages_directory_path: string
    :type other_pages_directory_path: string
    :return:
    """

    # Directory containing the PDF files
    pdf_directory = input_directory_path

    # Get a list of all PDF files in the directory
    pdf_files = [file for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

    # Loop through each PDF file
    for pdf_file in pdf_files:
        # Create the full path to the PDF file
        pdf_path = os.path.join(pdf_directory, pdf_file)

        # Convert the PDF file to images
        images = convert_from_path(
            pdf_path,
            grayscale=True,
            poppler_path=poppler_path
        )

        # Loop through each image and save it
        for i, image in enumerate(images):
            if i == 0:
                image.save(os.path.join(first_pages_directory_path, pdf_file + '_page_' + str(i + 1) + '.png'), 'PNG')
            else:
                image.save(os.path.join(other_pages_directory_path, pdf_file + '_page_' + str(i + 1) + '.png'), 'PNG')
