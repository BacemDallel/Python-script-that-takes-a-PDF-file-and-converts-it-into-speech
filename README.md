# PDF to Speech Converter

This Python script converts a PDF file into speech, providing an audio representation of the text within the PDF.

## Prerequisites

Before running the script, ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Additionally, install the required Python packages using pip:

```bash
pip install PyPDF2 pyttsx3
Usage
Clone or download this repository to your local machine.

Place the PDF file you want to convert into the same directory as the pdf_to_speech.py script.

Run the script using the following command:

bash
Copy code
python pdf_to_speech.py
Follow the instructions provided by the script. It will prompt you to enter the filename of the PDF you want to convert.

The script will read the PDF file and convert its contents into speech. You will hear the text being spoken aloud.

Configuration
You can adjust the speech rate by modifying the rate parameter in the script. The default rate is set to 150 words per minute. You can increase or decrease this value as needed.

python
Copy code
engine.setProperty('rate', 150)
Dependencies
PyPDF2: A Python library for reading and manipulating PDF files.
pyttsx3: A text-to-speech conversion library in Python.
