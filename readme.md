# Text-to-Speech GUI Application

This is a Python application that converts text from PDF and Word documents to speech and saves it as an audio file. The application provides a graphical user interface (GUI) built with Tkinter, allowing users to select a file, choose a voice (male or female), and generate an audio output.

## Features

- Convert text from PDF or Word documents to speech.
- Save the converted speech as an audio file in MP3 format.
- Choose between male and female voices for the output.
- Simple and intuitive GUI for easy interaction.

## Prerequisites

Before running the application, make sure you have Python installed on your system. You will also need to install the following Python packages:

- `tkinter` (included with most Python installations)
- `PyPDF2` (for reading PDF files)
- `pyttsx3` (for text-to-speech conversion)
- `python-docx` (for reading Word files)

You can install the necessary packages using pip:

```bash
pip install PyPDF2 pyttsx3 python-docx

How to Use
Run the Application:

Run the Python script:
python main.py

Select a File:

Click on the "Browse your file" button to select a PDF or Word document from your system.

Choose Voice:

Select either "Male voice" or "Female voice" from the checkboxes.

Convert and Save:

Click on "Create and save audio file" to convert the text to speech and save it as an audio.mp3 file.

Code Overview
The application uses the following libraries:

Tkinter: Provides the GUI components.
PyPDF2: Reads and extracts text from PDF files.
python-docx: Reads and extracts text from Word documents.
pyttsx3: Performs text-to-speech conversion.
Troubleshooting
No Text Content Found: Make sure the selected file is either a valid PDF or Word document and contains readable text.
Error Reading PDF or Word File: Ensure that the file is not corrupted and has readable text content.
Contributing
Contributions are welcome! If you have any suggestions, bug reports, or improvements, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
PyPDF2 for PDF file handling.
python-docx for Word document handling.
pyttsx3 for text-to-speech conversion.

