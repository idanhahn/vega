import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

blacklist = [
    '[document]', 'noscript', 'header',   'html', 'meta', 'head', 'input',
    'script', ]
# there may be more elements you don't want, such as "style", etc.


def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters


def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output


def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text = chap2text(html)
        Output.append(text)
    return Output


def convert_epub(input_file_path):

    chapters = epub2thtml(input_file_path)
    text = thtml2ttext(chapters)

    output_txt_file = open(input_file_path + '.txt', 'w')
    for t in text:
        output_txt_file.write(t)
    output_txt_file.close()
    return input_file_path.filename + '.txt'
