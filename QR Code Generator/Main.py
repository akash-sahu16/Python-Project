
import qrcode

def generate_qr_code(link):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

# Get link from user input
link = input("Enter the link: ")

# Generate QR code
qr_code = generate_qr_code(link)

# Save QR code as an image file
file_name = "qr_code.png"
qr_code.save(file_name)
print(f"QR code generated and saved as '{file_name}'")
