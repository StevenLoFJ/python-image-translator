from PIL import Image, ImageDraw, ImageFilter, ImageFont
from helper.image import readTextFromImage, blurImage
from helper.text import translateText
import time
def imageTranslator():

    image_path = 'test.png'
    
    image = Image.open(image_path)
    imgData = readTextFromImage(image)
    plainCanvas = ImageDraw.Draw(image)

    for i in range(len(imgData['text'])):
        if int(imgData['conf'][i]) > 50 and imgData['text'][i].isalpha():  # filter high confident & text only to be blur and translated 
            (x, y, w, h) = (imgData['left'][i], imgData['top'][i], imgData['width'][i], imgData['height'][i])
            textArea = [x, y, x + w, y + h]
            text_position = (x, y)
            text =  imgData['text'][i]
            blurImage(image,textArea)

            font_path = 'test.ttf'
            font_size = h *5/6
            font = ImageFont.truetype(font_path, font_size)
       
            plainCanvas.text(text_position, translateText(text), font=font, fill=(0, 0, 0))
    image.save('path_to_save_new_image.jpg')

imageTranslator()
time.sleep(1000)
            
