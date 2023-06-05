import os
from pdf2image import convert_from_path

# Directory containing the PDF files
pdf_directory = r'Articles_Examples'

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
        poppler_path=r"C:\Users\ariya\Downloads\Release-23.05.0-0\poppler-23.05.0\Library\bin"
    )

    # Loop through each image and save it
    for i, image in enumerate(images):
        if i == 0:
            image.save(os.path.join('labeled_data/first_pages', pdf_file + '_page_' + str(i + 1) + '.png'), 'PNG')
        else:
            image.save(os.path.join('labeled_data/other_pages', pdf_file + '_page_' + str(i + 1) + '.png'), 'PNG')
