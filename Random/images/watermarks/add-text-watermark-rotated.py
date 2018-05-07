
# https://stackoverflow.com/questions/245447/how-do-i-draw-text-at-an-angle-using-pythons-pil

from PIL import Image, ImageDraw, ImageFont, ImageOps

# add watermark to png image
def main():
    
    png_image = Image.open('nature.png')
    
    font = ImageFont.truetype('arial.ttf', 48)
    text = Image.new('L', (500, 500))
    draw = ImageDraw.Draw(text)
    draw.text((10, 10), 'Python Study Group', font=font, fill=100)
    rotated = text.rotate(20, expand=1)
    
    png_image.paste(ImageOps.colorize(rotated, (10, 10, 10), (25, 25, 25)), (242, 60), rotated)
    png_image.save('nature-watermark-rotated.png')
    

if __name__ == '__main__':
    
    main()
