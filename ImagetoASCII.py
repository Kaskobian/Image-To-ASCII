#Author: Kaskobi (Kaskobian Softworks LLC)
#Copywrite: Florida Institute of Technology Open Source Community
#Copywrite: MIT License

import sys
from PIL import Image

# Define the ASCII characters that will be used to construct the ASCII art
ASCII_CHARS = "@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# ANSI escape codes for colors
def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

# Map each RGB value to its corresponding ASCII character
def rgb_to_ascii(r, g, b):
    brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
    ascii_index = int((brightness * (len(ASCII_CHARS) - 1)) / 255)
    return ASCII_CHARS[ascii_index]

# Resize the image according to a new width, maintaining aspect ratio
def scale_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    resized_image = image.resize(new_dim)
    return resized_image

# Map pixels to ASCII characters and add color
def map_pixels_to_ascii_chars(image, new_width=100):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    pixels = list(image.getdata())
    ascii_str = ""
    for i in range(0, len(pixels), new_width):
        line = pixels[i:i+new_width]
        ascii_line = ""
        for r, g, b in line:
            ascii_line += rgb_to_ansi(r, g, b) + rgb_to_ascii(r, g, b)
        ascii_line += "\033[0m"
        ascii_str += ascii_line + "\n"
    return ascii_str

# The main function that will orchestrate the conversion
def main(image_path, width):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return

    image = scale_image(image, new_width=width)
    ascii_art = map_pixels_to_ascii_chars(image, new_width=width)
    print(ascii_art)

if __name__ == '__main__':
    # Default values but please change the path for the image that you need
    default_image_path = "G:\\Backup Downloads\\CustomEmblem-transformed.png"
    default_width = 100  # A more reasonable default width

    # Take the image path and the desired width from command line arguments, or use default values
    image_path = sys.argv[1] if len(sys.argv) > 1 else default_image_path
    width = int(sys.argv[2]) if len(sys.argv) > 2 else default_width

    main(image_path, width)
