from convertors.convert_pdf import convert_pdf
from convertors.convert_ebup import convert_epub


def convert(input_file_path):

    extension = input_file_path.split(".")[3]

    if extension == 'pdf':
        txt_file_path = convert_pdf(input_file_path)
    elif extension == 'docx':
        # convert_docx(file)
        pass
    elif extension == 'epub':
        txt_file_path = convert_epub(input_file_path)
    elif extension == 'mobi':
        # convert_mobi(file)
        pass

    return txt_file_path
