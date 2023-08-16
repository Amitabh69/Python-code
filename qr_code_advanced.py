                      ##   ADVANCED QR CODE

import qrcode
from PIL import Image
code=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
code.add_data("https://youtu.be/k783W5arEI4")
code.make(fit=True)
image=code.make_image(fill_color="green",back_color="white")
image.save("Advaced qr code.png")