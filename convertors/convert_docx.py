import pypandoc


def convert_docx (file):
  file_txt = pypandoc.convert_file(file, 'txt')
  
  output_txt = open(file + '.txt', 'w')
  for t in file_txt:
    output_txt.write(t)
  output_txt.close() 
  
  return file + '.txt'