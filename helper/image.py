from PIL import ImageFilter
import pytesseract

def readTextFromImage(image):
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # use this for windows
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract' # use this for dockerbuild
    data = pytesseract.image_to_data(image,config=r'--psm 6',output_type=pytesseract.Output.DICT)
    return data

def blurImage(image,textArea):
    croppedImage = image.crop(textArea)
    blured = croppedImage.filter(ImageFilter.BoxBlur(radius=100))
    image.paste(blured, textArea)