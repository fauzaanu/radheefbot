# create a python function that uses a font and generate an image
# with the text in the font

import PIL

from PIL import Image, ImageDraw, ImageFont
from main import get_radheef_val

def generate_image(word,meaning,extra_notes):
    # create an image with the text from the font with RTL support
    # and return the image

    font = ImageFont.truetype("fonts/Mvlhohi.ttf", 50)

    word_length = font.getsize(word)
    meaning_length = font.getsize(meaning)
    extra_notes_length = font.getsize(extra_notes)

    # based on the highest getsize of the text, create an image with the size
    # of the text
    # add 10 to the width and height to add some padding

    image = Image.new("RGB", (max(word_length[0],meaning_length[0],extra_notes_length[0])+10,1280), (0,0,0))
    draw = ImageDraw.Draw(image)

    # based on the length of the text, the position of the text should be dynamic and based on image size
    # so that the text is centered

    draw.text((image.width/2-word_length[0]/2,0),word,(255,255,255),font=font)
    draw.text((image.width/2-meaning_length[0]/2,word_length[1]),meaning,(255,255,255),font=font)
    draw.text((image.width/2-extra_notes_length[0]/2,word_length[1]+meaning_length[1]),extra_notes,(255,255,255),font=font, align="right")

    # do additional cropping to ensure there is no extra white space
    # crop any area where there is no white text

    # detect black pixels
    black_pixels = []
    for x in range(image.width):
        for y in range(image.height):
            if image.getpixel((x,y)) == (255,255,255):
                black_pixels.append((x,y))

    # get the min and max of the black pixels
    min_x = min(black_pixels,key=lambda x:x[0])[0]
    max_x = max(black_pixels,key=lambda x:x[0])[0]
    min_y = min(black_pixels,key=lambda x:x[1])[1]
    max_y = max(black_pixels,key=lambda x:x[1])[1]

    # crop the image
    image = image.crop((min_x,min_y,max_x,max_y))



    image.save('pil_text_font_v3.png')
    
# create a font object with the font file and specify
# desired size



if __name__ == "__main__":
    x = get_radheef_val("ދުނިޔެ")

    if x is not None:
        for y in x:
            generate_image(y['current_word_dv'],y['meaning_text'],y['extra_notes_dv'])
