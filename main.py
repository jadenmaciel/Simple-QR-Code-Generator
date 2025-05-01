import qrcode 

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=50,
                   border=10)

qr.add_data("https://www.neuralnine.com/books")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("advanced.png")