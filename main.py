import pyttsx3
from PyPDF2 import PdfReader


def pdf_to_speech(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PdfReader(file)

        # Initialize the text variable
        text = ""

        # Loop through each page and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Initialize the Text-to-Speech engine
    engine = pyttsx3.init()

    # Set properties for speech
    engine.setProperty('rate', 150)  # You can adjust the speech rate as needed

    # Convert text to speech
    engine.say(text)

    # Run the engine (starts speaking)
    engine.runAndWait()


# Provide the path to the PDF file you want to convert
pdf_file_path = 'Bacem_Dallel_CV.pdf'

# Call the function to convert PDF to speech
pdf_to_speech(pdf_file_path)
