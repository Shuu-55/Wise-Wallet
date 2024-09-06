import tabula

def convert_pdf_to_csv(pdf_file_path, csv_file_path):
    
    tabula.convert_into(pdf_file_path, csv_file_path, output_format="csv", pages="all")

if __name__ == "__main__":
    # Replace PDF_FILE_PATH with the path to the PDF file to convert.
    PDF_FILE_PATH = "C:\\Users\\H.P\\Downloads\\Shuu-500093945.pdf"

    # Replace CSV_FILE_PATH with the path to save the CSV file to.
    CSV_FILE_PATH = "output.csv"

    convert_pdf_to_csv(PDF_FILE_PATH, CSV_FILE_PATH)
