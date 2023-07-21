import os
import pandas as pd
from PyPDF2 import PdfReader, PdfWriter

def split_pdf_pages(input_pdf_path, output_folder, names_csv):
    # Make sure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the PDF
    pdf = PdfReader(input_pdf_path)

    # Load the csv/excel data
    names_df = pd.read_csv(names_csv) if names_csv.endswith('.csv') else pd.read_excel(names_csv)

    # Iterate through the PDF's pages
    for page_number in range(len(pdf.pages)):
        # Write each page to a separate PDF
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page_number])
        output_pdf_path = os.path.join(output_folder, names_df.iloc[page_number, 0] + '.pdf')

        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


# Use the function
split_pdf_pages('/Users/zaiddahir/Desktop/Test Canva/Student Name - Completion Certificate f.pdf', '/Users/zaiddahir/Desktop/Test Canva', '/Users/zaiddahir/Desktop/Test Canva/Names.csv')


