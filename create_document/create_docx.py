import docx


def generate_docx_document(file_name_docx, transcription: str):
    # escribimos el archivo .docx para enviarlo al usuario

    file_path: str = f"documents/{file_name_docx}.docx"

    # Crea un nuevo documento
    doc = docx.Document()

    # Agrega un párrafo al documento
    doc.add_paragraph(f"Texto del audio transcrito:\n\n{transcription}")

    # Guarda el documento en un archivo .docx
    doc.save(file_path)

    # Abrimos el archivo y lo enviamos
    file_docx = open(file_path, 'rb')

    return file_docx
