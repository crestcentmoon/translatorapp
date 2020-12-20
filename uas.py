import PIL
from PIL import Image
import pytesseract
from googletrans import Translator

fileimg = 'about_python.png'
targeted_image = Image.open(fileimg)
text = pytesseract.image_to_string(targeted_image)

print('Tulisan pada gambar:\n', text)

words = text.split()
print('\nJumlah kata pada gambar about_python')
print('adalah: ', len(words))

score = len(words)*10
print('Skor yang bisa didapatkan: $', score)

translator = Translator()
test1 = translator.translate(text, dest='id')
print('\nTerjemahan:\n', test1.text)

