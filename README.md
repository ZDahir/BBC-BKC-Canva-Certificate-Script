🎓 BBC-BKC-Canva Certificate Script

Split a master PDF from Canva into individual certificates for each student using this Python script.

---

 🚀 Features

- Automated Splitting: Convert a single master PDF into individual PDFs with ease.
- Custom Naming: Uses student names from a CSV to name each PDF file.

---

 🛠 Prerequisites

1. Python: Ensure Python is installed on your machine.
2. CSV File: Have a CSV file ready with all student names.
3. Canva Master PDF: The main PDF to be split. Rename it to 'input.pdf'.
4. Output Folder: A designated folder path to store all individual PDFs.
5. Required Packages: Install the necessary Python packages using the terminal or command prompt:
   
   ```bash
   pip install PyPDF2 pandas
   ```

---

 🔧 How to Use

1. Ensure you have all prerequisites set up.
2. Update the paths for the input PDF, output folder, and names CSV.
3. Run the function with the respective paths:
   
   ```python
   split_pdf_pages('input.pdf', 'output_folder', 'names.csv')
   ```

---

Happy Certificate Generation! 🎉
