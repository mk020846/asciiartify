from PIL import Image
from resize_image import resize_image
from grayify import grayify
from pixels_to_ascii import pixels_to_ascii
from save_to_file import save_to_file
#ASCII_CHARS = "@B%8WM#*oahkbdpwmZOOQJYXzcvnxrjft/\|()1{}[]-_+~<>i!1T;:,\"^`'."
ASCII_CHARS = ' ','\u2591','\u2592','\u2593','\u2588'
with open('logo.MD','r') as logo:
    print(logo.read())
def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image, ASCII_CHARS)
    save_to_file(ascii_str,new_width)

image_path = input("ENTER THE ABSOLUTE PATH FOR THE IMAGE YOU WANT TO CONVERT: ")
new_width = int(input("ENTER NEW WIDTH FOR THE IMAGE: "))
main(image_path,new_width=50)