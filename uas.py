import PIL
from PIL import Image
import pytesseract
from googletrans import Translator

fileimg = 'about_python.png'
targeted_image = Image.open(fileimg)
text = pytesseract.image_to_string(targeted_image)

print('Tulisan pada gambar:\n', text)

translator = Translator()
def trans():
    print('\n\t-----------------------------')
    print('\tKode Bahasa Tersedia')
    print('\t-------------------------------')
    print('\t1. Indonesia (id)')
    print('\t2. Perancis (fr)')
    print('\t3. Jerman (de)')
    print('\t-------------------------------')
    print('')
    
    pilih = input("Masukkan kode bahasa: ")
    
    if pilih == 'id':
        paragraph = translator.translate(text, dest='id')
        print('\nTerjemahan:\n', paragraph.text)
        tanya()
    elif pilih == 'fr':
        paragraph = translator.translate(text, dest='fr')
        print('\nTerjemahan:\n', paragraph.text)
        tanya()
    elif pilih == 'de':
        paragraph = translator.translate(text, dest='de')
        print('\nTerjemahan:\n', paragraph.text)
        tanya()
    else:
        print('Maaf, bahasa yang anda pilih belum tersedia')
        
def tanya():
    tanya = input('\n\tKembali ke menu utama? (y/t)')
    if tanya == 'y':
        trans()
    elif tanya == 't':
        exit
    else:
        print('\n\tWrong answer')
        
trans()

