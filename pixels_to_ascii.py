def pixels_to_ascii(image,ascii_chars):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        index = pixel_value * (len(ascii_chars)-1) // 255
        ascii_str += ascii_chars[index]
    return ascii_str