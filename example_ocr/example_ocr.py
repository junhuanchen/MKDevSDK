import pytesseract

# https://digi.bib.uni-mannheim.de/tesseract/
# see this tools

from PIL import Image
from PIL import ImageEnhance

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'

imgry = Image.open('ocr/value.png')

# im_size = image.size

# 裁剪图片
# imgry = image.crop((0, 0, 0, 0))

# 转化为灰度图
imgry = imgry.convert('L')

# 亮度增强
def Brightness(imgry, bright = 100):
    enhance_image = ImageEnhance.Brightness(imgry)
    return enhance_image.enhance(bright)

Brightness(imgry)

# imgry.show()

# 对比度增强
def Contrast(imgry, contrast = 100):
    enhance_image = ImageEnhance.Contrast(imgry)
    return enhance_image.enhance(contrast)

Contrast(imgry)

# imgry.show()

out = imgry


text = pytesseract.image_to_string(out, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789') #  -c tessedit_char_whitelist=0123456789

print(text)

out.show()

# 以后补上训练数据