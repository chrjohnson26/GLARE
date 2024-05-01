import pyautogui
import time
import cv2
import os
import numpy as np
from PIL import ImageGrab, Image
#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



def main():
    # initializing variables for image processing

    screenshot = pyautogui.screenshot()

    # specifiying the path to save the image
    # matthew macbook m2 air dimensions 2560 x 1664

    folder_path = "/Users/christianjohnson/Downloads/Glare/testPylonImages"

    # Provide the path to the folder containing images, desired output video name, and frame rate
    #image_folder = '/Users/christianjohnson/Downloads/Glare/Saved_Images'
    video_name = 'demoGLARE.mp4'
    fps = 10  # Adjust the frame rate as per your requirement

    images_to_video(folder_path, video_name, fps)





def overlay(img, array, jump):
    coord = universal_blocking(img,jump)
    for i in range(jump):
        for j in range(jump):
            array[(coord[0]+i),(coord[1]+j)] = 0
    array*=255
    im = Image.fromarray(array)
    imgplot = plt.imshow(im)


def images_to_video(folder_path, video_name, fps):
    images = [img for img in os.listdir(folder_path) if img.endswith(".tiff")]
    print(images)
    frame = cv2.imread(os.path.join(folder_path, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(folder_path, image)))

    cv2.destroyAllWindows()
    video.release()



"""
    universal_blocking takes an array of of any shape and a jump value. 
    It then finds the maximum average value of a block of size jump x jump
"""
def universal_blocking(array, jump):
    # Deriving the array demensions then trimming for ease of indexing
    r, c = array.shape
    r += r%10
    c -= c%10

    ar1 = np.arange(0,r, jump)
    print(ar1)
    ar2 = np.arange(0,c, jump)
    max_value = 0.
    coord = ()

    for i in ar1:
        for j in ar2:
            b_sum = 0
            for i2 in range(jump):
                for j2 in range(jump):
                    b_sum += array[i+i2][j+j2]
            current_average = b_sum/(jump^2)
            if(current_average > max_value):
                print(20, " ", current_average, (i, j))
                max_value = current_average
                coord=(i,j)
    return coord
