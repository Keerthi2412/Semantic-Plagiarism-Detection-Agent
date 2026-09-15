from pypdf import PdfReader
from docx import Document


def extract_text(file):

    filename = file.filename.lower()

    # TXT file
    if filename.endswith(".txt"):

        return file.read().decode("utf-8")


    # PDF file
    elif filename.endswith(".pdf"):

        reader = PdfReader(file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        return text


    # DOCX file
    elif filename.endswith(".docx"):

        document = Document(file)

        text = ""

        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                text += paragraph.text + "\n"

        return text


    else:

        raise ValueError(
            "Unsupported file format. Please upload PDF, DOCX or TXT."
        )


def split_into_sections(text):

    sections = []

    # Split using paragraphs
    paragraphs = text.split("\n")

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        # Ignore very short lines
        if len(paragraph) > 20:

            sections.append(paragraph)

    return sections
