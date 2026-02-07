import qrcode
from qrcode import QRCode
import os

def generateQrCode():
    url = "https://htb-pro.github.io/easyInviteSite/templates/index.html"
    filename = "easyInvite.png"
    folder_dir = "static/Pictures"
    file_path = os.path.join(folder_dir,filename)
    QR = QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size= 4,
        border = 2
    )
    QR.add_data(url)
    img = QR.make_image(fill_color="white", back_color = "black")
    img.save(file_path)

generateQrCode()