
import qrcode
from PIL import Image
import matplotlib.pyplot as plt
import sys


def gen_qr(url: str, size: int) -> Image.Image:
    """Create a high-quality QR code resized to the requested pixel size."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    return qr_image.resize((size, size), Image.Resampling.LANCZOS)

def open_bg():
     


def main():
	
	id = 'aa'
	qr_image = gen_qr(f'https://bikeclemson.github.io/qr?utm_source=qr&utm_medium=r{id}&utm_campaign=cu',400)

	plt.figure(figsize=(6, 6))
	plt.imshow(qr_image, cmap="gray")
	plt.axis("off")
	plt.tight_layout()
	plt.show()



    
	

if __name__ == "__main__":
    main()
