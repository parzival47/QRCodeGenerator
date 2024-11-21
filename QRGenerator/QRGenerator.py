#pip install pyqrcode

import pyqrcode


url = input("Enter Url to Generate QR Code:  ")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg', scale=5)