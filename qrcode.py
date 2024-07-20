
import qrcode

def generate_qr_code(data, filename):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)                                   

    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image
    img.save(filename)

    print("QR Code generated successfully!")  
if __name__ == "__main__":
    data = input("Enter the data for QR code: ")
    filename = input("Enter the filename for QR code (with extension): ")

    generate_qr_code(data, filename)
                                       