from colorama import Fore
from PIL import Image

def colored(R, G, B, text):                                                                 # adds colour to the ASCII characters to be printed
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(R, G, B, text)

ASCII_characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"    # list of ASCII characters in ascending order of brightness level

image_to_be_printed = Image.open("balloons.jpg")                                            # opened image

colour_or_not = str(input("Do you want the picture to be printed in colour?(y/n): "))       # asks user if the user wants to see the printed image in color or not

if colour_or_not == 'y':                                                                    #loop for printing the image in colour
    image_to_be_printed = image_to_be_printed.resize((200,75), Image.ANTIALIAS)
    w, h = image_to_be_printed.size
    for i in range(h):
        for j in range(w):
            image_RGB = image_to_be_printed.getpixel((j,i))
            R, G, B = image_RGB[0], image_RGB[1], image_RGB[2]
            avg = int(0.21*R + 0.72*G + 0.07*B)
            index = int((len(ASCII_characters)*avg)/256)
            print(colored(R, G, B, ASCII_characters[index]), end='')
        print('')
else:                                                                                       #loop for printing image in black and white
    image_to_be_printed = image_to_be_printed.resize((500,100), Image.ANTIALIAS)
    w, h = image_to_be_printed.size
    for i in range(h):
        for j in range(w):
            image_RGB = image_to_be_printed.getpixel((j,i))
            R, G, B = image_RGB[0], image_RGB[1], image_RGB[2]
            avg = int(0.21*R + 0.72*G + 0.07*B)
            index = int((len(ASCII_characters)*avg)/256)
            print(ASCII_characters[index], end='')
        print('') 