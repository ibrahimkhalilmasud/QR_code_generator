### need to install pip install pyqrcode
### pip install pypng

import os
import png
import pyqrcode
from PIL import Image


class QR_Gen(object):
    def __init__(self, text):
        self.image = self.generator(text)

    @staticmethod
    def generator(text):
        qr_code = pyqrcode.create(text)
        file_name = "QR Code Result"
        save_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        name = f"{save_path}{file_name}.png"
        qr_code.png(name, scale = 10)
        image = Image.open(name)
        image = image.resize((400,400), Image.ANTIALIAS)
        image.show()

if __name__ == "__main__":
    text = str(input("Enter text or Link: "))
    QR_Gen(text)
