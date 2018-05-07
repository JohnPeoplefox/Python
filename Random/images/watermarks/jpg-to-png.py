
from PIL import Image

# convert a jpg image to png
def main():
    
    jpg_image = Image.open('nature.jpg')
    png_image = jpg_image.convert('RGB')
    png_image.save('nature.png')
    

if __name__ == '__main__':
    
    main()
