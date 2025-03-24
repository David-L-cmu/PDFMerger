# PDF Merger

A simple GUI application for merging multiple PDF files into a single document.

## Features

- Select multiple PDF files to merge
- Rearrange the order of PDFs before merging
- Remove selected files from the list
- Automatically generate timestamped output filename or specify your own
- Choose where to save the merged PDF

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- PyPDF2

## Installation

1. Clone or download this repository

2. Install required dependencies:
```
pip install PyPDF2
```

## Usage

1. Run the application:
```
python pdf_merger_app.py
```

2. Click "Add PDFs" to select the PDF files you want to merge

3. Arrange the files in the desired order using "Move Up" and "Move Down" buttons

4. (Optional) Enter a name for the output file or leave blank for automatic naming

5. Click "Merge PDFs" and select where to save the merged file

6. The merged PDF will be saved to your chosen location

## Screenshot

![image](https://github.com/user-attachments/assets/15fb8460-72de-4a4d-95e3-36d90c879670)


## License
MIT License

Copyright (c) 2025 David-L-cmu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
