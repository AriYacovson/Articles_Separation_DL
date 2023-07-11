from tkinter import Tk, Label, Button, filedialog, Entry
from PyPDF2 import PdfReader, PdfWriter
import tensorflow as tf
from pdf2image import convert_from_path
import numpy as np
from pathlib import Path

THRESHOLD = "0.1"
BEGINNING = "0"
NUM_OF_ARTICLES="0"
MODEL = 'first_model.h5'


def split_by_points(input_path, page_numbers, beginning=0):
    page_numbers = [num+beginning for num in page_numbers]

    # Load the PDF file
    with open(input_path, 'rb') as file:
        pdf = PdfReader(file)

        # Create a PDF writer object
        pdf_writer = PdfWriter()

        start_page = beginning
        for end_page in page_numbers:
            # Add pages to the PDF writer object
            for page_num in range(start_page, end_page):
                pdf_writer.add_page(pdf.pages[page_num])

            # Save the extracted pages as a new PDF file
            output_path = f'output_{start_page + 1}_to_{end_page}.pdf'
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            # Clear the PDF writer for the next set of pages
            pdf_writer = PdfWriter()

            # Set the start page for the next iteration
            start_page = end_page

        # If there are remaining pages, add them to the last file
        if start_page < len(pdf.pages):
            for page_num in range(start_page, len(pdf.pages)):
                pdf_writer.add_page(pdf.pages[page_num])

            # Save the remaining pages as a new PDF file
            output_path = f'output_{start_page + 1}_to_end.pdf'
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)


def extract_split_points(pdf_path, model, beginning=0, thresh=0.5, number_of_articles=0):
    # Convert PDF page to image
    pages = convert_from_path(pdf_path, first_page=1)
    pages = pages[beginning:]

    all_images = []
    for page in pages:
        image = page  # Get the first page as an image

        # Convert the image to grayscale
        image = image.convert('L')

        # Preprocess the image
        image = image.resize((224, 224))  # Resize the image to match the model's input size
        image = tf.keras.preprocessing.image.img_to_array(image)  # Convert PIL Image to numpy array
        image = image / 255.0  # Normalize pixel values (assuming your model expects values in the range [0, 1])
        all_images.append(image)

    all_images = tf.convert_to_tensor(all_images)
    predictions = model.predict(all_images).reshape(-1)
    if number_of_articles > 0:
        indices = sorted(range(len(predictions)), key=lambda i: predictions[i], reverse=True)[:number_of_articles]
    else:
        indices = list(np.where(predictions > thresh)[0])
    print(indices)
    return sorted(indices)


def split_book_to_articles(model_name, pdf_path, beginning, thresh, num_of_articles):
    # Load the CNN model
    model = tf.keras.models.load_model(model_name)
    split_pages = extract_split_points(pdf_path, beginning=beginning, model=model, thresh=thresh,
                                       number_of_articles=num_of_articles)

    # Call the function to split the PDF
    split_by_points(pdf_path, split_pages, beginning=beginning)


def main():
    root = Tk()

    def browse_file():
        filename = filedialog.askopenfilename(initialdir="/", title="Select PDF file", filetypes=(("PDF files", "*.pdf"),
                                                                                                  ("All files", "*.*")))
        pdf_path_entry.delete(0, 'end')
        pdf_path_entry.insert(0, filename)

    def split_button_click():
        pdf_path = Path(pdf_path_entry.get())  # Use pathlib.Path for file path
        thresh = float(thresh_entry.get())
        beginning = int(beginning_entry.get())
        num_of_articles = int(num_of_articles_entry.get())
        model_name = MODEL

        # splitting the book to articles
        split_book_to_articles(model_name, pdf_path, beginning, thresh, num_of_articles)

        # Close the GUI window
        root.destroy()


    # GUI Setup
    root.title("PDF Splitter")
    root.geometry("400x200")

    pdf_path_label = Label(root, text="PDF Path:")
    pdf_path_label.pack()

    pdf_path_entry = Entry(root)
    pdf_path_entry.pack()

    browse_button = Button(root, text="Browse", command=browse_file)
    browse_button.pack()

    thresh_label = Label(root, text="Threshold:")
    thresh_label.pack()

    thresh_entry = Entry(root)
    thresh_entry.insert(0, THRESHOLD)
    thresh_entry.pack()

    beginning_label = Label(root, text="Beginning:")
    beginning_label.pack()

    beginning_entry = Entry(root)
    beginning_entry.insert(0, BEGINNING)
    beginning_entry.pack()

    num_of_articles_label = Label(root, text="Number of Articles:")
    num_of_articles_label.pack()

    num_of_articles_entry = Entry(root)
    num_of_articles_entry.insert(0, NUM_OF_ARTICLES)
    num_of_articles_entry.pack()

    split_button = Button(root, text="Split PDF", command=split_button_click)
    split_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()