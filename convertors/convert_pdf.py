from pdfminer.high_level import extract_text


def convert_pdf(input_file_path):
    text = extract_text(input_file_path)
    output_txt_file = open(input_file_path + '.txt', 'w')
    for t in text:
        output_txt_file.write(t)
    output_txt_file.close()
    return input_file_path + '.txt'
