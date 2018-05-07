
# https://gist.github.com/snay2/876425

from PIL import Image, ImageDraw, ImageFont, ImageFilter

# add watermark to png image
def main():
    
    png_image = Image.open('nature.png')
    width, height = png_image.size
    
    watermark = Image.new('RGBA', png_image.size)
    watermark_draw = ImageDraw.ImageDraw(watermark, 'RGBA')

    text = 'Py Study Group'
    font = ImageFont.truetype('arial.ttf', 48)
    
    watermark_draw.text((20, 20), text, font=font)
    #opacity mask
    mask = watermark.convert('L').point(lambda x: min(x, 100))
    watermark.putalpha(mask)
    embossed = watermark.filter(ImageFilter.EMBOSS)
    png_image.paste(embossed, None, embossed)
    png_image.save('nature-watermark-emboss.png')
    

if __name__ == '__main__':
    
    main()
