from os.path import exists
import random
filenamesrc = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
def create_filename():
    filename = ''
    for i in range(random.randint(5,20)):
        filename += random.choice(filenamesrc)
    return filename
def main():
    filename = create_filename()
    while True:
        if exists(filename):
            pass
        else:
            return filename + '.MD'
def save_to_file(ascii_str,new_width):
    with open(main(),'a') as output_file:
        for i in range(0,len(ascii_str), new_width):
            output_file.write(ascii_str[i:i+new_width]+'\n')
        output_file.close()