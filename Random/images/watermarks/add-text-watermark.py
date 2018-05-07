
from PIL import Image, ImageDraw, ImageFont

# add watermark to png image
def main():
    
    png_image = Image.open('nature.png')
    width, height = png_image.size
    
    watermark = ImageDraw.Draw(png_image)

    text = 'Py Study Group'
    font = ImageFont.truetype('arial.ttf', 48)
    textwidth, textheight = watermark.textsize(text, font)
    
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    
    watermark.text((x, y), text, font=font)
    png_image.save('nature-watermark.png')
    

if __name__ == '__main__':
    
    main()
