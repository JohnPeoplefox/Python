
import cv2
import imageio


# Extract each 20th frame
FRAME = 20
# x scaling factor
FX = 0.2
# y scaling factor
FY = 0.2


# Extract each 20th frame from the clip
# and save them in the current directory
# Return a list with saved image names
def extract_frames(movie_name):


    images = []
    vidcap = cv2.VideoCapture(movie_name)
    success,image = vidcap.read()

    count = 0
    success = True

    while success:
        
        success,src_image = vidcap.read()
        
        if count % FRAME == 0:
            dest_image = cv2.resize(src_image, (0, 0),  fx=FX, fy=FY)
            cv2.imwrite("frame%d.jpg" % count, dest_image)
            images.append(imageio.imread("frame%d.jpg" % count))
        
        count += 1
        
    return images


# Create animated gif from saved images
def create_gif(images):
    imageio.mimsave('movie.gif', images)    


def main():

    # http://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_5mb.mp4
    movie_name = 'big_buck_bunny_720p_5mb.mp4'
    images = extract_frames(movie_name)
    create_gif(images)


if __name__ == '__main__':
    main()
