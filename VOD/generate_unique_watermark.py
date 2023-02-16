import hashlib
from PIL import Image, ImageDraw, ImageFont

# import EAN13 from barcode module
from barcode import EAN13

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

# Importing library
import qrcode


def generate_watermark(subscriber_info):
    # Create a hash value based on the subscriber's information
    hash_value = hashlib.sha1(subscriber_info.encode()).hexdigest()
    #hash_value = hashlib.sha256(subscriber_info.encode()).hexdigest()
    
    # Load the original watermark image
    original_image = Image.open("original_watermark.png")
    
    # Create a unique watermark image for each subscriber
    width, height = original_image.size
    unique_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(unique_image)
    font = ImageFont.truetype("arial.ttf", 110)
    draw.text((100, height/2+100), hash_value, font=font, fill=(255, 0, 0, 128), stroke_width=5)
    
    # Overlay the unique watermark on the original image
    result = Image.alpha_composite(original_image, unique_image)
    
    # Save the result as a PNG file
    result.save("unique_watermark_{}.png".format(hash_value))
    
    return hash_value

def hash_to_barcode(hash_code):
    barcode = ''
    for char in hash_code:
        char_code = ord(char)
        barcode += str(char_code)
    return barcode

def main():
    id="umersub"
    hash_code=generate_watermark(id)

# Make sure to pass the number as string

# Data to be encoded
    data = hash_code
    img2=qrcode.make(id)
# Encoding data using make() function
    img = qrcode.make(data)

# Saving as an image file
    img.save('MyQRCode1.png')
    img2.save("og.png")
    barcode = hash_to_barcode(hash_code)
    print(barcode)

# Now, let's create an object of EAN13 class and
# pass the number with the ImageWriter() as the
# writer
    my_code = EAN13(barcode, writer=ImageWriter())

# Our barcode is ready. Let's save it.
    my_code.save("new_code1")

if __name__ == "__main__":
    main()